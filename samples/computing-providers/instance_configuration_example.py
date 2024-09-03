import pprint

from swan import Orchestrator

def instance_configuration(instance_type: str) -> dict:
    """Retrieve currently avaliable orchestrator cp resources (instance).

    Args:
        avalibility: True for availiable instance configuration only; False for all configuration.

    Return:
        A list of dictionary of Swan Instance CP configuration Info.
    """
    # Create Orchestrator instance.
    so = Orchestrator(api_key=None, login=False)
    # Retrieve all CP resources.
    avaliable_resources = so.get_instance_resources(available=False)
    instance_config = [resource for resource in avaliable_resources if resource['instance_type'] == instance_type][0]
    return instance_config

def display_config_info(instance_config: dict):
    """Display detailed explaination of instance configuration.

    Instance Type: Name of the instance configuration. Indicate the computational power of the hardware.
    Hardware ID: Internal ID for the hardware configuration on Swan Chain (Used for API and Smartcontract).
    Price: SwanToken per hours for running the instance with given configuration.
    Region: Geological regions the given instance type is avaliable in.
    Type: Computation resource type; CPU or GPU.
    Status: If any hardwares under the instance type is avaliable. Used to find avaliable hardwares.
    Description: A brief summary of the instance's configurations.

    Args:
        instance_config: dictionary of instance configuration details.
    """
    # Instance type
    print(f'\x1b[6;30;42minstance_type (Name):\x1b[0m {instance_config['instance_type']}')
    # Important information
    print('\x1b[0;30;44mImportant Information (Affect Task Deployment)\x1b[0m')
    print(f'\x1b[0;30;41mhardware_id (ID for smart contracts and APIs):\x1b[0m {instance_config['hardware_id']}')
    print(f'\x1b[0;30;41mprice (SwanToken/hr):\x1b[0m {instance_config['price']}')
    print(f'\x1b[0;30;41mregion (Currently availiable regions):\x1b[0m {instance_config['region']}')
    # Other information
    print('\x1b[0;30;44mOther Information (Useful Knowledge)\x1b[0m')
    print(f'\x1b[0;30;43mtype (CPU or GPU):\x1b[0m {instance_config['type']}')
    print(f'\x1b[0;30;43mstatus (If any hardwares are avaliable):\x1b[0m {instance_config['status']}')
    print(f'\x1b[0;30;43mdescription (Brief summary of instance config):\x1b[0m {instance_config['description']}')

if __name__ == '__main__':
    instance_type = 'G1ae.small'
    # Avaliable resources
    instance_config = instance_configuration(instance_type=instance_type)
    # Output the first instance configuration on the list
    display_config_info(instance_config=instance_config)