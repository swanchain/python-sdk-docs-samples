import os
import dotenv
import logging
import json
import sys

import swan
from swan import Orchestrator
from swan.object import TaskRenewalResult


def setup(swan_api_key: str) -> Orchestrator:
    """Setup required informations for task deployment.

    Args:
        swan_api_key: Swan Orchestrator API key.
    
    Return:
        Swan Orchestrator object connected to Swan Orchestrator APIs.
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
        duration:int=3600
    ) -> TaskRenewalResult:
    """Extend an existing task with UUID.

    Args:
        swan_orchestrator: Orchestrator object connect through API key.
        private_key: Users Web3 wallet prviate address for signing message/signature.
        task_uuid: task UUID of an existing task.
        duration: additional duration to for task extension.

    Return:
        TaskRenewalResult.
    """
    result = swan_orchestrator.renew_task(
        task_uuid=task_uuid, 
        private_key=private_key, 
        duration=duration,
    )
    return result


if __name__ == '__main__':
    dotenv.load_dotenv()

    if len(sys.argv) != 2:
        logging.error("Usage: python renew_task.py <task_uuid>")
        sys.exit(1)

    task_uuid = sys.argv[1]

    swan_api_key = os.getenv("SWAN_API_KEY")
    wallet_address = os.getenv("WALLET_ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")

    # Connect to Orchestrator
    swan_orchestrator = setup(swan_api_key)

    # Extend existing task
    renew_result = extend_task_duration(
        swan_orchestrator=swan_orchestrator, 
        private_key=private_key, 
        task_uuid=task_uuid
    )
    if renew_result:
        logging.info(json.dumps(renew_result.to_dict(), indent=2, ensure_ascii=False))
        logging.info(f'Task {task_uuid} renew request success.')
    else:
        logging.error(f'Task {task_uuid} renew request failed.')