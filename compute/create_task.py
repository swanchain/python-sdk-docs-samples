import logging
import time
import json

import swan
from swan import Orchestrator

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
    return wallet_address, private_key, swan_orchestrator

def deploy_task(repo_uri: str, wallet_address: str, private_key: str, swan_orchestrator: Orchestrator) -> dict:
    """Deploy a task to Swan Chain.

    Args:
        repo_uri: URI of the repo for deployment (must contain .yaml or Dockerfile for docker build/docker-compose).
        wallet_address: Users Web3 wallet address.
        private_key: Users Web3 wallet prviate address for signing message/signature.
        swan_orchestrator: Orchestrator object connect through API key.

    Return:
        Detailed task informations.
    """
    # Create a new task
    result = swan_orchestrator.create_task(
        repo_uri=repo_uri,
        wallet_address=wallet_address,
        private_key=private_key,
        instance_type='C1ae.small',
        auto_pay=True
    )
    # Check task uuid (Unique Identifier)
    # Task UUID is required for checking and performing futher operation on the created tasks.
    # Remember to store task UUID after deployment.
    task_uuid = result['task_uuid']
    # Retrieve task information (UUID, task detail, instance configuration, etc)
    task_info = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
    return task_info

def store_task_info_to_json(task_info: dict, directory: str, indent:int=2):
    """Save task infomation into a JSON file!
    """
    # Store json file 
    with open(directory, 'w') as file:
        json.dump(task_info, file, indent=indent)

def wait_for_deployment(swan_orchestrator: Orchestrator, task_uuid: str, max_wait_minute: int) -> list:
    """A function to wait until task are successfully deployed (Running).

    Args:
        swan_orchestrator: Orchestrator object connect through API key.
        task_uuid: task UUID of deployed task.
        max_wait_minute: Maximum mintues to be waited.
    """
    # wait for app URLs be generated
    app_urls = []
    total_wait_time = 0
    while True:
        time.sleep(5)
        total_wait_time += 5
        if app_urls := swan_orchestrator.get_real_url(task_uuid=task_uuid):
            logging.info(f"App will be running at {app_urls}")
            break
        if total_wait_time > 3600 * max_wait_minute:
            logging.info(f"Waited more than {max_wait_minute} minutes. Function stopped.")
            break

if __name__ == '__main__':
    # Repo URI for deployment (A simple Hello World! Can be replaced with custom test repo.)
    repo_uri = 'https://github.com/swanchain/awesome-swanchain/tree/main/hello_world'

    swan_api_key = '<swan_api_key>'
    wallet_address = '<wallet_address>'
    private_key = '<private_key>'
    # Connect to Orchestrator
    swan_orchestrator = setup(swan_api_key)

    # Deploy task
    result = deploy_task(
        repo_uri=repo_uri, 
        wallet_address=wallet_address, 
        private_key=private_key, 
        swan_orchestrator=swan_orchestrator
    )
    print(f'Task Created, UUID: \x1b[6;30;42m{result['data']['task']['uuid']}\x1b[0m')

    # Save task information for future use
    store_task_info_to_json(task_info=result['data']['task'], directory='./task_info.json')

    # Wait for deployment
    wait_minutes = 5
    wait_for_deployment(
        swan_orchestrator=swan_orchestrator, 
        task_uuid=result['data']['task']['uuid'], 
        max_wait_minute=wait_minutes
    )