import pytest
import subprocess
import logging


def test_get_instance_resources_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/get_instance_resources.py"], capture_output=True, text=True)
    
    print(result.stderr)
    assert "Available Instance types: [\'" in result.stderr