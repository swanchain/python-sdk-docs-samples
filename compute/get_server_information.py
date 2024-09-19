import json
import os
from typing import List
import dotenv
import logging
import swan
from swan import Orchestrator
from swan.object import InstanceResource, TaskDeploymentInfo


def setup_swan_orchestrator():
    # Initialize the Swan Orchestrator with API key and network
    swan_orchestrator = swan.resource(
        api_key=os.getenv("SWAN_API_KEY"), 
        service_name='Orchestrator'
    )
    return swan_orchestrator

# Get available instance resources
def get_instance_resources():
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    available_instances: List[InstanceResource] = swan_orchestrator.get_instance_resources()
    res_dict = [res.to_dict() for res in available_instances] if available_instances else []
    logging.info(json.dumps(res_dict, indent=2, ensure_ascii=False))

# Get all instance list
def get_instance_resources_all():
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    all_instances: List[InstanceResource] = swan_orchestrator.get_instance_resources(False)
    res_dict = [res.to_dict() for res in all_instances] if all_instances else []
    logging.info(json.dumps(res_dict, indent=2, ensure_ascii=False))

# Get existing task info
def get_task_info(task_uuid):
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    task_info: TaskDeploymentInfo = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
    logging.info(json.dumps(task_info.to_dict(), indent=2))


if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv()
    # get_instance_resources_all()
    get_instance_resources()
    # get_task_info("5f9d2925-bf55-4cb3-b829-20935b011ce1")