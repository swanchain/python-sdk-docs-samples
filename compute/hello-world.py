import os
import time
import dotenv
import logging
import asyncio
import aiohttp
import json

import swan
from swan import Orchestrator
from swan.object import TaskCreationResult, TaskDeploymentInfo

from base import ExampleBase

class HelloWorld(ExampleBase):
            
    def deploy(self):
        result: TaskCreationResult = self.orchestrator.create_task(
            repo_uri='https://github.com/swanchain/awesome-swanchain/tree/main/hello_world',
            wallet_address=os.getenv("WALLET_ADDRESS"),
            private_key=os.getenv("PRIVATE_KEY"),
            instance_type='C1ae.small',
            # duration=3600,                            # default 3600 seconds
            # preferred_cp_list=['cp_account_address']  # only the first one is used
            # ip_whitelist=['ip_address_1']
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

    hello_world = HelloWorld()
    hello_world.deploy()
    hello_world.wait_for_running()