import os
import dotenv
import logging
import time
import json
from typing import Optional
import asyncio
import aiohttp

import swan
from swan import Orchestrator
from swan.object import TaskCreationResult, TaskDeploymentInfo


def setup(swan_api_key: str):
    """Setup required informations for task deployment.

    SWAN_API_KEY: Swan Orchestrator API key.
    WALLET_ADDRESS: Users Web3 wallet address.
    PRIVATE_KEY: Users Web3 wallet prviate address for signing message/signature.
    """
    # Connect to Orchestrator
    swan_orchestrator = swan.resource(
        api_key=swan_api_key, 
        service_name='Orchestrator'
    )
    return swan_orchestrator


def deploy_task(
        repo_uri: str, 
        wallet_address: str, 
        private_key: str, 
        swan_orchestrator: Orchestrator) -> Optional[TaskCreationResult]:
    """Deploy a task to Swan Chain.

    Args:
        repo_uri: URI of the repo for deployment (must contain .yaml or Dockerfile for docker build/docker-compose).
        wallet_address: Users Web3 wallet address.
        private_key: Users Web3 wallet prviate address for signing message/signature.
        swan_orchestrator: Orchestrator object connect through API key.

    Return:
        TaskCreationResult.
    """
    # Create a new task
    task_result: TaskCreationResult = swan_orchestrator.create_task(
        repo_uri=repo_uri,
        wallet_address=wallet_address,
        private_key=private_key,
        instance_type='C1ae.small',
        region='global',
        duration=3600
    )
    # Check task uuid (Unique Identifier)
    # Task UUID is required for checking and performing futher operation on the created tasks.
    # Remember to store task UUID after deployment.
    task_uuid = task_result.task_uuid if task_result else None
    tx_hash = task_result.tx_hash if task_result else None
    logging.info(f'Task creation result: {task_result}')
    if not task_uuid:
        logging.error(f"\x1b[31mFailed to initialize task.\x1b[0m")
        return task_result
    if not tx_hash:
        logging.error("\x1b[31mFailed to create task, transaction hash not found.\x1b[0m")
        return task_result
    logging.info(f'Task created successfully, next step to check its deployment status.')
    logging.info(f'UUID: \x1b[6;30;42m{task_uuid}\x1b[0m')
    return task_result


def store_task_info_to_json(task_info: dict, directory: str, indent:int=2):
    """Save task infomation into a JSON file!
    """
    # Store json file 
    with open(directory, 'w') as file:
        json.dump(task_info, file, indent=indent)


def wait_for_deployment(
        swan_orchestrator: Orchestrator, 
        task_uuid: str, 
        max_wait_minute: int) -> Optional[TaskDeploymentInfo]:
    """A function to wait until task are successfully deployed (Running).
    
    Args:
        swan_orchestrator: Orchestrator object connect through API key.
        task_uuid: task UUID of deployed task.
        max_wait_minute: Maximum mintues to be waited.

    Return:
        TaskDeploymentInfo.
    """

    timeout_for_waiting = max_wait_minute * 60
    start_time = time.time()
    while True:
        time.sleep(5)
        task_deploy_info: TaskDeploymentInfo = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
        if task_deploy_info.jobs:
            logging.info(f"Task is deployed successfully, next step to check its instance applications.")
            return task_deploy_info
        if time.time() - start_time > timeout_for_waiting:
            logging.error(f"Timeout for waiting, it may take longer time to deploy.")
            return task_deploy_info


def waiting_for_running(
        swan_orchestrator: Orchestrator, 
        task_uuid: str, 
        max_wait_minute: int) -> list:
    timeout_for_waiting = max_wait_minute * 60
    app_urls = []
    if app_urls := swan_orchestrator.get_real_url(task_uuid=task_uuid):
        logging.info(f"App will be running at {app_urls}")
        async def wait_for_url(url):
            start_time = time.time()
            async with aiohttp.ClientSession() as session:
                # after 5 minutes, assume app url is not running
                while time.time() - start_time < timeout_for_waiting:
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
    else:
        logging.error(f"App URL not found, it may take longer time to deploy.")
    return app_urls


if __name__ == '__main__':
    dotenv.load_dotenv()
    # Repo URI for deployment (A simple Hello World! Can be replaced with custom test repo.)
    repo_uri = 'https://github.com/swanchain/awesome-swanchain/tree/main/hello_world'

    swan_api_key = os.getenv("SWAN_API_KEY")
    wallet_address = os.getenv("WALLET_ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")
    # Connect to Orchestrator
    swan_orchestrator: Orchestrator = setup(swan_api_key)

    # Deploy task
    task_result: TaskCreationResult = deploy_task(
        repo_uri=repo_uri, 
        wallet_address=wallet_address, 
        private_key=private_key, 
        swan_orchestrator=swan_orchestrator
    )

    task_uuid = task_result.task_uuid
    tx_hash = task_result.tx_hash

    if task_uuid and tx_hash:
        # Save task creation information for future use
        store_task_info_to_json(task_info=task_result.to_dict(), directory='./task_creation_info.json')

        # Wait for deployment
        wait_minutes = 5
        task_deployment_result: TaskDeploymentInfo = wait_for_deployment(
            swan_orchestrator=swan_orchestrator, 
            task_uuid=task_uuid, 
            max_wait_minute=wait_minutes
        )

        # Save task deployment information for future use
        store_task_info_to_json(task_info=task_deployment_result.to_dict(), directory='./task_deployment_info.json')

        # Wait for running
        wait_minutes = 5
        app_urls = waiting_for_running(
            swan_orchestrator=swan_orchestrator, 
            task_uuid=task_uuid, 
            max_wait_minute=wait_minutes
        )
