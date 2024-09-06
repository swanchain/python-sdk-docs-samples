import swan
from swan import Orchestrator


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
        service_name='Orchestrator'
    )
    return swan_orchestrator

def verify_connection(swan_orchestrator: Orchestrator):
    """Verification to secure connection.
    """
    return swan_orchestrator.get_contract_info()

if __name__ == '__main__':
    swan_api_key = '<swan_api_key>'
    swan_orchestrator = login_to_swan_orchestrator_through_api_key(swan_api_key=swan_api_key)
    # Make sure connected to correct Orchestrator backend API.
    print(f'Connected to \x1b[6;30;42m{swan_orchestrator.swan_url}\x1b[0m')

    verification = verify_connection(swan_orchestrator=swan_orchestrator)
    if verification:
        print('Connected to Swan mainnet.')