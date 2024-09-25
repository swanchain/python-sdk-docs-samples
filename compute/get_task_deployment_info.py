import json
import os
import dotenv
import logging
import swan
from swan import Orchestrator
from swan.object import TaskDeploymentInfo


def setup_swan_orchestrator():
    """
    Initialize the Swan Orchestrator with API key and network.
    """
    swan_orchestrator = swan.resource(
        api_key=os.getenv("SWAN_API_KEY"), 
        service_name='Orchestrator'
    )
    return swan_orchestrator

def get_task_info(task_uuid):
    """
    Get the task deployment information.
    """
    swan_orchestrator: Orchestrator = setup_swan_orchestrator()
    task_info: TaskDeploymentInfo = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
    logging.info(json.dumps(task_info.to_dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv()
    # task_uuid = '5f9d2925-bf55-4cb3-b829-20935b011ce1'
    task_uuid = '<TASK_UUID>'
    get_task_info(task_uuid)