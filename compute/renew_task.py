import swan
from swan import Orchestrator
import swan

def setup(swan_api_key: str):
    """Setup required informations for task deployment.

    SWAN_API_KEY: Swan Orchestrator API key.
    WALLET_ADDRESS: Users Web3 wallet address.
    PRIVATE_KEY: Users Web3 wallet prviate address for signing message/signature.
    """
    # Connect to Orchestrator
    swan_orchestrator = swan.resource(
        api_key="Z926BmQJyp", 
        service_name='Orchestrator',
        network='testnet'
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
    task_uuid = '78ae584a-712d-4cb9-8e59-34f7ca23724d'
    # instance_type has to be same as the originals
    instance_type = 'C1ae.small'

    swan_api_key = "Z926BmQJyp"
    wallet_address = "0xCA8609D14f48E59323702d1c945dBb145a87D27D"
    private_key = "3b7a2af605e336ffa60891a387c2fabad4f1900a88993f150dac933dd66f5f99"
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