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
    result = swan_orchestrator.renew_payment(
        task_uuid=task_uuid, 
        private_key=private_key, 
        duration=duration,
        instance_type=instance_type
    )
    return result

if __name__ == '__main__':
    # Input task UUID
    task_uuid = '<uuid>'
    # instance_type has to be same as the originals
    instance_type = '<instance_type>'

    swan_api_key = '<swan_api_key>'
    wallet_address = '<wallet_address>'
    private_key = '<private_key>'
    # Connect to Orchestrator
    swan_orchestrator = setup(swan_api_key)

    # Extend existing task
    tx_hash = extend_task_duration(
        swan_orchestrator=swan_orchestrator, 
        private_key=private_key, 
        task_uuid=task_uuid,
        instance_type=instance_type
    )
    print(f'Task renewed! Payment Tx Hash: \x1b[6;30;42m{tx_hash}\x1b[0m')