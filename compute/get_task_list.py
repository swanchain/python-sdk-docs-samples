import json
import os
import dotenv
import logging
import swan
from swan import Orchestrator
from swan.object import TaskList


def setup_swan_orchestrator():
    """
    Initialize the Swan Orchestrator with API key and network.
    """
    swan_orchestrator = swan.resource(
        api_key=os.getenv("SWAN_API_KEY"), 
        service_name='Orchestrator',
        network='testnet'
    )
    return swan_orchestrator

def get_task_list():
    """
    Get the list of tasks under the wallet address and user implied by the API key.
    """
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    result: TaskList = swan_orchestrator.get_task_list(
        wallet_address=os.getenv("WALLET_ADDRESS"),
        page=1,
        size=2
    )
    logging.info(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv()
    get_task_list()