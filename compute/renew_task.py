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
    task_uuid = 'f1c6d8f5-f2bb-4ba9-9a41-045bb787fa8a'
    # instance_type has to be same as the originals
    instance_type = 'C1ae.small'

    swan_api_key = 'd7odWACgJH'
    wallet_address = '0x61c3e03dbed55f5DE213732e816F8A8Fd6E9bfF0'
    private_key = '9b7b90e22f0ac48611e4c9e9a09b008c013780a8bb28e213b60e5ad15953258c'
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