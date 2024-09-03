import pprint
from swan import Orchestrator

def base_orchestrator_connection() -> Orchestrator:
    # Create Orchestrator instance.
    # For acquiring CP informations, login/authenication is not required.
    so = Orchestrator(api_key=None, login=False)
    return so

def search_hardware_id_with_instance_type(instance_type: str, swan_orchestrator: Orchestrator) -> int:
    """Find the hardward_id of the given instance_type.

    Args:
        instance_type: the name of the instance type from Swan Orchestrator.

    Return:
        Integer hardware_id
    """
    hardware_id = swan_orchestrator.get_instance_hardware_id(instance_type=instance_type)
    return hardware_id

def search_instance_price_with_instance_type(instance_type: str, swan_orchestrator: Orchestrator) -> int:
    """Find the hardward_id of the given instance_type.

    Args:
        instance_type: the name of the instance type from Swan Orchestrator.

    Return:
        Integer instance price
    """
    # Retrieve hardware id .
    hardware_id = swan_orchestrator.get_instance_price(instance_type=instance_type)
    return hardware_id

if __name__ == '__main__':
    so = base_orchestrator_connection()
    intance_type = 'G1ae.small'

    # Search hardware id
    hardware_id = search_hardware_id_with_instance_type(instance_type=intance_type, swan_orchestrator=so)
    print(f'Hardware ID for {intance_type}: {hardware_id}')

    # Search instance price
    instance_price = search_instance_price_with_instance_type(instance_type=intance_type, swan_orchestrator=so)
    print(f'Instance price for {intance_type}: {instance_price}')