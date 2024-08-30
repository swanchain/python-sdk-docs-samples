import os

import dotenv
import swan



def hello_world():
    orchestrator = swan.resource(api_key=os.getenv("SWAN_API_KEY"), network='mainnet',service_name='Orchestrator')

    result = orchestrator.create_task(
        app_repo_image='hello_world',
        wallet_address=os.getenv("WALLET_ADDRESS"),
        private_key=os.getenv("PRIVATE_KEY"),
    )
    task_uuid = result['id']
    task_info = orchestrator.get_deployment_info(task_uuid=task_uuid)
    print(task_info)

if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv("../.env")
    hello_world()