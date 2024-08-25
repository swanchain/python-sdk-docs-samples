import json
import os
import pytest
import pandas as pd

import dotenv
import swan


@pytest.fixture
def setup_swan_orchestrator():
    # Load environment variables from the .env file
    dotenv.load_dotenv()
    # Initialize the Swan Orchestrator with API key and network
    swan_orchestrator = swan.resource(api_key=os.getenv("SWAN_API_KEY"), network='mainnet', service_name='Orchestrator')
    return swan_orchestrator


def test_get_hardware_id_list(setup_swan_orchestrator):
    swan_orchestrator = setup_swan_orchestrator
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

    df = pd.DataFrame(rows)

    # Display the DataFrame as a table
    print(df)


def test_get_task_infot(setup_swan_orchestrator):
    swan_orchestrator = setup_swan_orchestrator
    task_info = swan_orchestrator.get_deployment_info(task_uuid="f7495e02-9b93-4701-9421-13347f597b4d")
    print(json.dumps(task_info, indent=2))
