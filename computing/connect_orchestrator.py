import os

from dotenv import load_dotenv

import swan
from swan import Orchestrator

def load_environmenat_variables() -> str:
    """Load Swan API key from .env file.

    Return: swan_api_key (Do not share with others)
    """
    # Load environment variables from .env file
    load_dotenv()
    swan_api_key = os.getenv('SWAN_API_KEY')
    return swan_api_key

def login_to_swan_orchestrator_through_api_key(swan_api_key: str) -> Orchestrator:
    """Login into Swan Orchestractor with API Key.

    Args:
        swan_api_key

    Return:
        Swan Orchestrator object connected to Swan Orchestrator APIs.
    """
    # Create Orchestrator instance.
    swan_orchestrator = swan.resource(
        api_key=swan_api_key, 
        network='mainnet', 
        service_name='Orchestrator'
    )
    return swan_orchestrator

def verify_connection(swan_orchestrator: Orchestrator):
    """Verification to secure connection.
    """
    return swan_orchestrator.get_contract_info()

if __name__ == '__main__':
    swan_api_key = load_environmenat_variables()
    swan_orchestrator = login_to_swan_orchestrator_through_api_key(swan_api_key=swan_api_key)
    # Make sure connected to correct Orchestrator backend API.
    print(f'Connected to \x1b[6;30;42m{swan_orchestrator.swan_url}\x1b[0m')

    verification = verify_connection(swan_orchestrator=swan_orchestrator)
    if verification:
        print('Connected to Swan mainnet.')