import pprint
from swan import Orchestrator

def orchestrator_cp_resources(avaliability:bool=True) -> list[dict]:
    """Retrieve currently avaliable orchestrator cp resources (instance).

    Args:
        avalibility: True for availiable instance configuration only; False for all configuration.

    Return:
        A list of dictionary of Swan Instance CP configuration Info.
    """
    # Create Orchestrator instance.
    so = Orchestrator(api_key=None, login=False)
    # Retrieve avaliable resources. (CPs that are currently avaliable)
    avaliable_resources = so.get_instance_resources(available=avaliability)
    return avaliable_resources

if __name__ == '__main__':
    # Avaliable resources
    result = orchestrator_cp_resources()
    # Output the first instance configuration on the list
    pprint.pprint(result[:1])