import json
import logging
import os

import dotenv
from swan.object import TaskCreationResult, TaskDeploymentInfo
from swan.object.task_spec import HardwareSpec, GpuSpec, TaskSpecFactory

from base import ExampleBase

DOCKERFILE_CONTENT = """
# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Create the index.html file with the desired content
RUN echo "dockerfile testing success" > index.html

# Expose port 8000 for the HTTP server
EXPOSE 8000

# Start the HTTP server when the container launches
CMD ["python3", "-m", "http.server", "8000"]
"""

class HelloWorld(ExampleBase):

    def deploy(self):
        dockerfile_task_spec = TaskSpecFactory.build_dockerfile_task(
            hardware_spec=HardwareSpec(
                cpu=2,
                memory=4,
                storage=30,
                gpus=[
                    GpuSpec(
                        gpu_model="NVIDIA 3080",
                        count=1,
                    )
                ]
            ),
            dockerfile_content=DOCKERFILE_CONTENT,
        )

        result: TaskCreationResult = self.orchestrator.create_task(
            base_task_spec=dockerfile_task_spec,
            wallet_address=os.getenv("WALLET_ADDRESS"),
            private_key=os.getenv("PRIVATE_KEY"),
            duration=3600,
        )
        self.task_uuid = result.task_uuid if result else None
        self.tx_hash = result.tx_hash if result else None
        if not self.task_uuid:
            logging.error(f"\x1b[31mFailed to initialize task.\x1b[0m")
            return
        if not self.tx_hash:
            logging.error("\x1b[31mFailed to create task, transaction hash not found.\x1b[0m")
            return
        task_info: TaskDeploymentInfo = self.orchestrator.get_deployment_info(task_uuid=self.task_uuid)
        logging.info(task_info)
        logging.info(f"\x1b[32mtask_uuid:\x1b[0m \x1b[6;30;42m{self.task_uuid}\x1b[0m")
        return result
    
    def get_deployment_info(self):
        task_info: TaskDeploymentInfo = self.orchestrator.get_deployment_info(task_uuid=self.task_uuid)
        return task_info

    @staticmethod
    def store_task_info_to_json(task_info: dict, directory: str, indent:int=2):
        """Save task infomation into a JSON file!
        """
        # Store json file 
        with open(directory, 'w') as file:
            json.dump(task_info, file, indent=indent)
            logging.info(f"{directory} saved!")



if __name__ == "__main__":
    dotenv.load_dotenv()
    logging.basicConfig(level=logging.INFO)

    hello_world = HelloWorld()
    task_result: TaskCreationResult = hello_world.deploy()

    hello_world.store_task_info_to_json(task_info=task_result.to_dict(), directory='task_creation_info.json')

    hello_world.wait_for_running(timeout_deploy=10, timeout_running=5)

    task_info: TaskDeploymentInfo = hello_world.get_deployment_info()

    hello_world.store_task_info_to_json(task_info=task_info.to_dict(), directory='task_deployment_info.json')
