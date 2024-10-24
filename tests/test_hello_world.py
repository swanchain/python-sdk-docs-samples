import pytest
import subprocess
import logging


def test_hello_world_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/hello-world.py"], capture_output=True, text=True)
    
    print(result.stderr)
    assert "App is running successfully" in result.stderr