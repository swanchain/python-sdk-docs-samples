import os
import time
import dotenv
import logging
import asyncio
import aiohttp
import json

import swan
from swan import Orchestrator
from swan.object import TaskCreationResult, TaskDeploymentInfo

class HelloWorld:
    def __init__(self):
        self.orchestrator = swan.resource(
            api_key=os.getenv("SWAN_API_KEY"), 
            service_name='Orchestrator',
            network='testnet'
        )
            
    def deploy(self):
        result: TaskCreationResult = self.orchestrator.create_task(
            repo_uri='https://github.com/swanchain/awesome-swanchain/tree/main/hello_world',
            wallet_address=os.getenv("WALLET_ADDRESS"),
            private_key=os.getenv("PRIVATE_KEY"),
            instance_type='C1ae.small'
        )
        self.task_uuid = result.task_uuid if result else None
        self.tx_hash = result.tx_hash if result else None
        if not self.task_uuid:
            logging.error(f"\x1b[31mFailed to initialize task.\x1b[0m")
            return
        if not self.tx_hash:
            logging.error("\x1b[31mFailed to create task, transaction hash not found.\x1b[0m")
            return
        task_info: TaskDeploymentInfo = self.orchestrator.get_deployment_info(task_uuid=self.task_uuid)
        logging.info(task_info)
        logging.info(f"\x1b[32mTask is created successfully with task_uuid:\x1b[0m \x1b[6;30;42m{self.task_uuid}\x1b[0m")

    def wait_for_running(self, timeout_deploy=20, timeout_running=5):
        """Wait for the app to be running.
        
        Args:
            timeout_deploy: Timeout for deployment in minutes.
            timeout_running: Timeout for app to be running in minutes.
        """
        if not self.task_uuid or not self.tx_hash:
            return
        # wait for app URLs be generated
        app_urls = []
        timeout_for_deployment = timeout_deploy * 60   # waiting time for deployment
        start_time = time.time()
        while True:
            time.sleep(5)
            task_deploy_info: TaskDeploymentInfo = self.orchestrator.get_deployment_info(task_uuid=self.task_uuid)
            if task_deploy_info.jobs:
                if app_urls := self.orchestrator.get_real_url(task_uuid=self.task_uuid):
                    logging.info(f"App will be running at {app_urls}")
                    break
            # after timeout, stop waiting, anyway, the task may be still deploying
            # you can check the task deployment info via `get_deployment_info` 
            if time.time() - start_time > timeout_for_deployment:
                logging.info(f"{task_deploy_info}")
                logging.error(f"Timeout for deployment, please check the task deployment.")
                return
        
        # wait for app to be running
        async def wait_for_url(url):
            start_time = time.time()
            async with aiohttp.ClientSession() as session:
                # after timeout, assume app url is not running
                while time.time() - start_time < timeout_running * 60:
                    async with session.get(url) as resp:
                        if resp.status == 200:
                            logging.info(f"\x1b[32mApp is running at\x1b[0m \x1b[6;30;42m{url}\x1b[0m")
                            logging.info(f"Response: {await resp.text()}")
                            break
                        await asyncio.sleep(5)
                else:
                    logging.warning(f"App is not running at {url} after 5 minutes")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*[wait_for_url(url) for url in app_urls]))


if __name__ == "__main__":
    dotenv.load_dotenv()

    hello_world = HelloWorld()
    hello_world.deploy()
    hello_world.wait_for_running()