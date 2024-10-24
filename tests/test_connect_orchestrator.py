import pytest
import subprocess
import logging


def test_connect_orchestrator_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/connect_orchestrator.py"], capture_output=True, text=True)
    
    print(result.stderr)
    assert "Connected to Swan Orchestrator" in result.stderr