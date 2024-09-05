import json
from swan import Orchestrator

def orchestrator_cp_resources(availability:bool=True) -> list[dict]:
    """Retrieve currently available orchestrator cp resources (instance).

    Args:
        avalibility: True for availiable instance configuration only; False for all configuration.

    Return:
        A list of dictionary of Swan Instance CP configuration Info.
    """
    # Create Orchestrator instance.
    swan_orchestrator = Orchestrator(api_key=None, login=False)
    # Retrieve available resources. (CPs that are currently available)
    available_resources = swan_orchestrator.get_instance_resources(available=availability)
    return available_resources

if __name__ == '__main__':
    # Available resources
    result = orchestrator_cp_resources()
    # Output the first instance configuration on the list
    print(json.dumps(result[:1], indent=2, ensure_ascii=False))