import json
import os

import dotenv
import swan

def setup_swan_orchestrator():
    # Initialize the Swan Orchestrator with API key and network
    swan_orchestrator = swan.resource(api_key=os.getenv("SWAN_API_KEY"), network='mainnet', service_name='Orchestrator')
    return swan_orchestrator


def get_hardware_id_list():
    swan_orchestrator = setup_swan_orchestrator()
    available_hardware = swan_orchestrator.get_hardware_config()
    # Process JSON data into a DataFrame
    rows = []
    for instance in available_hardware:
        if isinstance(instance["region"], list):  # Check if region is a list
            for region in instance["region"]:
                rows.append({
                    "ID": instance["id"],
                    "Name": instance["name"],
                    "Description": instance["description"],
                    "Type": instance["type"],
                    "Region": region,
                    "Price": instance["price"],
                    "Status": instance["status"]
                })
        else:
            # Handle the case where region is a string or other type
            rows.append({
                "ID": instance["id"],
                "Name": instance["name"],
                "Description": instance["description"],
                "Type": instance["type"],
                "Region": instance["region"],  # Just take the string directly
                "Price": instance["price"],
                "Status": instance["status"]
            })

    # Display the DataFrame as a table
    print(rows)


def get_task_info(task_uuid):
    swan_orchestrator = setup_swan_orchestrator()
    task_info = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
    print(json.dumps(task_info, indent=2))


if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv("../.env")
    get_hardware_id_list()
    get_task_info("5f9d2925-bf55-4cb3-b829-20935b011ce1")