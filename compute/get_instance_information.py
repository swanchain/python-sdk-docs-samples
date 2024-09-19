from swan import Orchestrator

def swan_orchestrator_connection() -> Orchestrator:
    # Create Orchestrator instance.
    # For acquiring CP informations, login/authenication is not required.
    swan_orchestrator = Orchestrator(api_key=None, login=False)
    return swan_orchestrator


def search_instance_price_with_instance_type(instance_type: str, swan_orchestrator: Orchestrator) -> int:
    """Find the hardward_id of the given instance_type.

    Args:
        instance_type: the name of the instance type from Swan Orchestrator.

    Return:
        Integer instance price
    """
    # Retrieve instance price.
    instance_price = swan_orchestrator.get_instance_price(instance_type=instance_type)
    return instance_price


if __name__ == '__main__':
    swan_orchestrator = swan_orchestrator_connection()
    intance_type = 'G1ae.small'

    # Search instance price
    instance_price = search_instance_price_with_instance_type(instance_type=intance_type, swan_orchestrator=swan_orchestrator)
    print(f'Instance price for {intance_type}: {instance_price}')