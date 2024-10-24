import pytest
import subprocess
import logging


def test_instance_config_example_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/instance_configuration_example.py"], capture_output=True, text=True)
    
    print(result.stderr)
    assert "price (SwanToken/hr)" in result.stderr