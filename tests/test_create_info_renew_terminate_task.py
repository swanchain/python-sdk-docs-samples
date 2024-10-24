import pytest
import subprocess
import logging

task_uuid = None

def test_create_task_output(caplog):
    global task_uuid
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/create_task.py"], capture_output=True, text=True)
    
    # get the task_uuid
    part = result.stderr.split("task_uuid='")[1]
    task_uuid = part.split("'")[0].strip()

    print(result.stderr)
    assert "App is running successfully" in result.stderr

def test_task_info_output(caplog):
    assert task_uuid is not None, "No task_uuid"

    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/get_task_deployment_info.py", task_uuid], capture_output=True, text=True)
    
    print(result.stderr)
    assert "successfully" in result.stderr

def test_task_renew_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/renew_task.py", task_uuid], capture_output=True, text=True)
    
    print(result.stderr)
    assert "renew request success" in result.stderr

def test_task_terminate_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/terminate_task.py", task_uuid], capture_output=True, text=True)
    
    print(result.stderr)
    assert "termination request success" in result.stderr