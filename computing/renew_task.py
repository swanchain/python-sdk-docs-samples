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

def extend_task_duration(
        swan_orchestrator: Orchestrator, 
        private_key: str, 
        task_uuid: str, 
        instance_type: str, 
        duration:int=60
    ) -> str:
    """Extend an existing task with UUID.

    Args:
        swan_orchestrator: Orchestrator object connect through API key.
        private_key: Users Web3 wallet prviate address for signing message/signature.
        task_uuid: task UUID of an existing task.
        duration: additional duration to for task extension.

    Return:
        Payment Tx Hash.
    """
    result = swan_orchestrator.renew_payment(
        task_uuid=task_uuid, 
        private_key=private_key, 
        duration=duration,
        instance_type=instance_type
    )
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
    instance_type = data['task_detail']['hardware']

    # Connect to Orchestrator
    wallet_address, private_key, swan_orchestrator = setup()

    # Extend existing task
    tx_hash = extend_task_duration(
        swan_orchestrator=swan_orchestrator, 
        private_key=private_key, 
        task_uuid=task_uuid,
        instance_type=instance_type
    )
    print(f'Task renewed! Payment Tx Hash: \x1b[6;30;42m{tx_hash}\x1b[0m')