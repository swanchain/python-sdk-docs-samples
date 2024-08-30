import os
import time
import dotenv
import swan



def hello_world():
    orchestrator = swan.resource(api_key=os.getenv("SWAN_API_KEY"), network='mainnet',service_name='Orchestrator')

    result = orchestrator.create_task(
        repo_uri='https://github.com/swanchain/awesome-swanchain/tree/main/hello_world',
        wallet_address=os.getenv("WALLET_ADDRESS"),
        private_key=os.getenv("PRIVATE_KEY"),
        instance_type='C1ae.small',
        auto_pay=True
    )
    task_uuid = result['id']
    task_info = orchestrator.get_deployment_info(task_uuid=task_uuid)
    print(task_info)

    # Wait for the task to be deployed
    time.sleep(30)
    # Show deployed application URLs
    app_urls = orchestrator.get_real_url(task_uuid=task_uuid)
    print(f"App URLs: {app_urls}")

if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv("../.env")
    hello_world()