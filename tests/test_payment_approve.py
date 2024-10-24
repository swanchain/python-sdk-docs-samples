import pytest
import subprocess
import logging


def test_payment_approve_output(caplog):
    with caplog.at_level(logging.INFO):
        result = subprocess.run(["python", "compute/payment_approve.py"], capture_output=True, text=True)
    
    print(result.stderr)
    assert "Approving in advance (in ether), amount=" in result.stderr