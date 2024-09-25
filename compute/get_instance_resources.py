import json
import os
from typing import List
import dotenv
import logging
import swan
from swan import Orchestrator
from swan.object import InstanceResource


def setup_swan_orchestrator():
    """
    Initialize the Swan Orchestrator with API key and network.
    """
    swan_orchestrator = swan.resource(
        api_key=os.getenv("SWAN_API_KEY"), 
        service_name='Orchestrator'
    )
    return swan_orchestrator


def get_instance_resources_available():
    """
    Get the available instance resources.
    """
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    available_instances: List[InstanceResource] = swan_orchestrator.get_instance_resources()
    res_dict = [res.to_dict() for res in available_instances] if available_instances else []
    logging.info(json.dumps(res_dict, indent=2, ensure_ascii=False))

    instance_types = [res.instance_type for res in available_instances] if available_instances else []
    logging.info(f'Available Instance types: {instance_types}')


def get_instance_resources_all():
    """
    Get all instance resources.
    """
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    all_instances: List[InstanceResource] = swan_orchestrator.get_instance_resources(False)
    res_dict = [res.to_dict() for res in all_instances] if all_instances else []
    logging.info(json.dumps(res_dict, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv()
    # get_instance_resources_all()
    get_instance_resources_available()