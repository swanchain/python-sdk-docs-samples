import os
import dotenv
import logging
import json

from swan.object import TaskCreationResult, TaskDeploymentInfo, GPUSelectionList, CustomInstanceResult

from base import ExampleBase


class CustomInstance(ExampleBase):

    def check_gpu_selection_list(self):
        region = 'global'
        res: GPUSelectionList = self.orchestrator.get_gpu_selection_list(region)
        if res:
            logging.info(json.dumps(res.to_dict(), indent=2, ensure_ascii=False))
        else:
            logging.error("Failed to get GPU selection list.")

    def set_and_check_custom_instance(self):
        region = 'global' #'Quebec-CA'
        self.custom_instance = {
            "cpu": 2,
            "memory": 2,
            "storage": 5,
            "gpu_model": "NVIDIA 3080",
            "gpu_count": 1
        }
        res: CustomInstanceResult = self.orchestrator.get_custom_instance_result(self.custom_instance, region)
        if res:
            logging.info(json.dumps(res.to_dict(), indent=2, ensure_ascii=False)) 
        else:
            logging.error("Failed to get custom instance result.")

    def deploy(self):
        result: TaskCreationResult = self.orchestrator.create_task(
            repo_uri='https://github.com/swanchain/awesome-swanchain/tree/main/MusicGen',
            wallet_address=os.getenv("WALLET_ADDRESS"),
            private_key=os.getenv("PRIVATE_KEY"),
            custom_instance=self.custom_instance
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


if __name__ == "__main__":
    dotenv.load_dotenv()

    ex = CustomInstance()
    ex.check_gpu_selection_list()
    ex.set_and_check_custom_instance()
    ex.deploy()
    ex.wait_for_running(timeout_deploy=20, timeout_running=10)
