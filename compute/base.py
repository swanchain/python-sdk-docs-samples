import os
import time
import dotenv
import logging
import asyncio
import aiohttp
import json
import abc

import swan
from swan import Orchestrator
from swan.object import TaskCreationResult, TaskDeploymentInfo

class ExampleBase:
    def __init__(self):
        self.orchestrator = swan.resource(
            api_key=os.getenv("SWAN_API_KEY"), 
            service_name='Orchestrator',
            network='testnet'
        )
        self.task_uuid = None
        self.tx_hash = None

    @abc.abstractmethod
    def deploy(self):
        raise NotImplementedError

    async def wait_for_url(self, url: str, timeout_minutes: int) -> bool:
        start_time = time.time()
        timeout_seconds = timeout_minutes * 60

        async with aiohttp.ClientSession() as session:
            while time.time() - start_time < timeout_seconds:
                try:
                    async with session.get(url, timeout=10) as resp:
                        if resp.status == 200:
                            logging.info(f"\x1b[32mApp is running at\x1b[0m \x1b[6;30;42m{url}\x1b[0m")
                            return True
                except aiohttp.ClientError as e:
                    logging.debug(f"Error connecting to {url}")
                except asyncio.TimeoutError:
                    logging.debug(f"Timeout connecting to {url}")
                except Exception as e:
                    logging.debug(f"An error occurred when accessing {url}. {e}")
                
                await asyncio.sleep(5)
            
            logging.warning(f"App is not running at {url} after {timeout_minutes} minutes")
            return False

    async def wait_for_deployment(self, timeout_deploy: int) -> list:
        timeout_for_deployment = timeout_deploy * 60
        start_time = time.time()

        app_urls = []
        task_deploy_info = None
        while time.time() - start_time < timeout_for_deployment:
            task_deploy_info: TaskDeploymentInfo = self.orchestrator.get_deployment_info(task_uuid=self.task_uuid)
            if task_deploy_info.task.status == "failed":
                logging.info(f"{task_deploy_info}")
                logging.error(f"\x1b[31mTask deployment failed.\x1b[0m")
                break
            if task_deploy_info.task.status == "completed":
                for job in task_deploy_info.jobs:
                    if job.job_real_uri:
                        app_urls.append(job.job_real_uri)
                if app_urls:
                    logging.info(f"{task_deploy_info}")
                    logging.info(f"\x1b[32mTask is deployed successfully, next step to check its instance applications.\x1b[0m")
                    logging.info(f"App will be running at {app_urls}")
                    break
            await asyncio.sleep(5)
        else:
            logging.info(f"{task_deploy_info}")
            logging.error(f"\x1b[38;5;208mTimeout for deployment, please check the task deployment.\x1b[0m")

        return app_urls

    async def wait_for_running_async(self, timeout_deploy: int, timeout_running: int):
        if not self.task_uuid or not self.tx_hash:
            return

        app_urls = await self.wait_for_deployment(timeout_deploy)
        if not app_urls:
            return

        tasks = [self.wait_for_url(url, timeout_running) for url in app_urls]
        results = await asyncio.gather(*tasks)

        for url, is_running in zip(app_urls, results):
            if is_running:
                logging.info(f"App is running successfully: {url}")
            else:
                logging.warning(f"App is not running ({url}) after {timeout_running} minutes")

    def wait_for_running(self, timeout_deploy=20, timeout_running=5):
        """Wait for the app to be running.
        
        Args:
            timeout_deploy: Timeout for deployment in minutes.
            timeout_running: Timeout for app to be running in minutes.
        """
        try:
            asyncio.run(self.wait_for_running_async(timeout_deploy, timeout_running))
        except Exception as e:
            logging.error(f"An error occurred while waiting for the app to run. {e}")


if __name__ == "__main__":
    print("This is the base class for the examples, providing helper functions.")
    print("It is not meant to be run directly.")
    print("Please run one of the example scripts instead.")