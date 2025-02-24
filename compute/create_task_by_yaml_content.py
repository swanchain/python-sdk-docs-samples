import json
import logging
import os

import dotenv
from swan.object import TaskCreationResult, TaskDeploymentInfo
from swan.object.task_spec import HardwareSpec, GpuSpec, TaskSpecFactory

from base import ExampleBase

YAML_CONTENT = """
version: "2.0"
services:
 image: alex6nbai/gpu_benchmark:20250219-4
 envs:
  - NCCL_P2P_DISABLE=1
  - NCCL_SHM_DISABLE=1
 expose_port:
  - 8000
"""

class HelloWorld(ExampleBase):

    def deploy(self):
        yaml_task_spec = TaskSpecFactory.build_yaml_task(
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
            yaml_content=YAML_CONTENT,
        )

        result: TaskCreationResult = self.orchestrator.create_task(
            base_task_spec=yaml_task_spec,
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
