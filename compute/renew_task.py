import logging
import os

import dotenv
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
    return swan_orchestrator

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

    api_result = swan_orchestrator.renew_task(
        task_uuid=task_uuid,
        private_key=private_key,
        auto_pay=True,
        instance_type=instance_type,
        duration=duration,
    )
    logging.info(f"{api_result=}")
    return api_result["tx_hash"]

if __name__ == '__main__':
    dotenv.load_dotenv("../.env")

    # Input task UUID
    task_uuid = '<task_uuid>'
    # instance_type has to be same as the originals
    instance_type = '<instance_type>'

    swan_api_key = os.getenv("SWAN_API_KEY")
    wallet_address = os.getenv("WALLET_ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")
    # Connect to Orchestrator
    swan_orchestrator = setup(swan_api_key)

    # Extend existing task
    tx_hash = extend_task_duration(
        swan_orchestrator=swan_orchestrator, 
        private_key=private_key, 
        task_uuid=task_uuid,
        instance_type=instance_type,
        duration=3600,
    )
    print(f'Task renewed! Payment Tx Hash: \x1b[6;30;42m{tx_hash}\x1b[0m')
