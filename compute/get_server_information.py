import json
import os

import dotenv
import swan

def setup_swan_orchestrator():
    # Initialize the Swan Orchestrator with API key and network
    swan_orchestrator = swan.resource(api_key="Z926BmQJyp", service_name='Orchestrator', network='testnet')
    return swan_orchestrator

# Get available instance resources
def get_instance_resources():
    swan_orchestrator = setup_swan_orchestrator()
    available_instances = swan_orchestrator.get_instance_resources()
    print(available_instances)

# Get all instance list
def get_instance_resources_all():
    swan_orchestrator = setup_swan_orchestrator()
    all_instances = swan_orchestrator.get_instance_resources(False)
    print(all_instances)

# Get existing task info
def get_task_info(task_uuid):
    swan_orchestrator = setup_swan_orchestrator()
    task_info = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
    print(task_info)


if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv("../.env")
    # get_instance_resources_all()
    get_instance_resources()
    get_task_info("5f9d2925-bf55-4cb3-b829-20935b011ce1")