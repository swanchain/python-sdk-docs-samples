import json
import logging
from typing import List
from swan import Orchestrator
from swan.object import InstanceResource


def orchestrator_cp_resources(availability: bool=True) -> List[InstanceResource]:
    """Retrieve currently available orchestrator cp resources (instance).

    Args:
        avalibility: True for availiable instance configuration only; False for all configuration.

    Return:
        A list of dictionary of Swan Instance CP configuration Info.
    """
    # Create Orchestrator instance.
    swan_orchestrator = Orchestrator(api_key=None, login=False)
    # Retrieve available resources. (CPs that are currently available)
    available_resources: List[InstanceResource] = swan_orchestrator.get_instance_resources(available=availability)
    return available_resources


if __name__ == '__main__':
    # Available resources
    result: List[InstanceResource] = orchestrator_cp_resources()
    # Output the first instance configuration on the list
    result_dict = [res.to_dict() for res in result] if result else []
    instance_types = [res.instance_type for res in result] if result else []
    logging.info(f'Available instance types: {len(instance_types)}')
    logging.info(f'Instance types: {instance_types}')
    logging.info(json.dumps(result_dict, indent=2, ensure_ascii=False))