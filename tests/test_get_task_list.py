import pytest
import subprocess
import logging


def test_get_task_list_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/get_task_list.py"], capture_output=True, text=True)
    
    print(result.stderr)
    assert "fetch task list for user successfully" in result.stderr