import os
import json

from dotenv import load_dotenv

import swan
from swan import Orchestrator

def setup():
    """Setup required informations for task deployment.

    SWAN_API_KEY: Swan Orchestrator API key.
    WALLET_ADDRESS: Users Web3 wallet address.
    PRIVATE_KEY: Users Web3 wallet prviate address for signing message/signature.
    """
    # Load .env into environment variables
    load_dotenv()
    # Get required information from environment variables
    swan_api_key = os.getenv('SWAN_API_KEY')
    wallet_address=os.getenv("WALLET_ADDRESS")
    private_key=os.getenv("PRIVATE_KEY")
    # Connect to Orchestrator
    swan_orchestrator = swan.resource(
        api_key=swan_api_key, 
        network='mainnet', 
        service_name='Orchestrator'
    )
    return wallet_address, private_key, swan_orchestrator

def terminate_existing_task(swan_orchestrator: Orchestrator, task_uuid: str):
    """Create a task early termination request.

    Args:
        swan_orchestrator: Orchestrator object connect through API key.
        task_uuid: task UUID of an existing task.

    Return:
        API response.
    """
    # Create a termiantion request.
    # Task will be termiated soon.
    result = swan_orchestrator.terminate_task(task_uuid=task_uuid)
    return result

if __name__ == '__main__':
    # Load task UUID
    # Using task info from samples/computing-tasks/create_task.py
    # Can be replace with other running task UUID
    try:
        directory = './task_info.json'
        with open(directory, 'r') as file:
            data = json.load(file)
    except:
        pass
    task_uuid = data['uuid']

    # Connect to Orchestrator
    wallet_address, private_key, swan_orchestrator = setup()

    # Terminate existing task
    result = terminate_existing_task(swan_orchestrator=swan_orchestrator, task_uuid=task_uuid)
    print(json.dumps(result, indent=2, ensure_ascii=False))