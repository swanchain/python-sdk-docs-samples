import logging

from swan import Orchestrator
from swan.object import InstanceResource


def instance_configuration(instance_type: str) -> InstanceResource:
    """Retrieve currently available orchestrator cp resources (instance).

    Args:
        avalibility: True for availiable instance configuration only; False for all configuration.

    Return:
        A list of dictionary of Swan Instance CP configuration Info.
    """
    # Create Orchestrator instance.
    swan_orchestrator = Orchestrator(api_key=None, login=False)
    # Retrieve all CP resources.
    available_resources = swan_orchestrator.get_instance_resources(available=False)
    instance_config = [resource for resource in available_resources if resource['instance_type'] == instance_type][0]
    return instance_config


def display_config_info(instance_config: dict):
    """Display detailed explaination of instance configuration.

    Instance Type: Name of the instance configuration. Indicate the computational power of the instance.
    Price: SwanToken per hours for running the instance with given configuration.
    Region: Geological regions the given instance type is available in.
    Type: Computation resource type; CPU or GPU.
    Status: If any instances under the instance type is available. Used to find available instances.
    Description: A brief summary of the instance's configurations.

    Args:
        instance_config: dictionary of instance configuration details.
    """
    # Instance type
    logging.info(f"\x1b[6;30;42minstance_type (Name):\x1b[0m {instance_config['instance_type']}")
    # Important information
    logging.info("\x1b[0;30;44mImportant Information (Affect Task Deployment)\x1b[0m")
    logging.info(f"\x1b[0;30;41mprice (SwanToken/hr):\x1b[0m {instance_config['price']}")
    logging.info(f"\x1b[0;30;41mregion (Currently availiable regions):\x1b[0m {', '.join(instance_config['region'])}")
    # Other information
    logging.info("\x1b[0;30;44mOther Information (Useful Knowledge)\x1b[0m")
    logging.info(f"\x1b[0;30;43mtype (CPU or GPU):\x1b[0m {instance_config['type']}")
    logging.info(f"\x1b[0;30;43mstatus (If any instances are available):\x1b[0m {instance_config['status']}")
    logging.info(f"\x1b[0;30;43mdescription (Brief summary of instance config):\x1b[0m {instance_config['description']}")


if __name__ == '__main__':
    instance_type = 'P1ae.xlarge'
    # available resources
    instance_config = instance_configuration(instance_type=instance_type)
    # Output the first instance configuration on the list
    display_config_info(instance_config=instance_config)