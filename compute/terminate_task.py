import os
import dotenv
import json
import logging

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
    dotenv.load_dotenv()
    # Input task UUID
    task_uuid = '<task_uuid>'

    swan_api_key = os.getenv("SWAN_API_KEY")
    # Connect to Orchestrator
    swan_orchestrator = setup(swan_api_key)

    # Terminate existing task
    result = terminate_existing_task(swan_orchestrator=swan_orchestrator, task_uuid=task_uuid)
    if result:
        logging.info(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        logging.info(f'Task {task_uuid} termination request success.')
    else:
        logging.error(f'Task {task_uuid} termination request failed.')