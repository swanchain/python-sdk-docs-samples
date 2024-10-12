"""
This example shows how to approve an allowance amount in advance. 
"""

import os
import dotenv
import swan
import logging

class ApproveAllowance:
    def __init__(self):
        self.orchestrator = swan.resource(
            api_key=os.getenv("SWAN_API_KEY"), 
            service_name='Orchestrator'
        )
    
    def approve(self):
        result = self.orchestrator.approve_allowance(
            private_key=os.getenv("PRIVATE_KEY"),
            amount=2
        )
        logging.info(result)

    def get_allowance(self):
        result = self.orchestrator.get_allowance(
            private_key=os.getenv("PRIVATE_KEY")
        )
        logging.info(result)


    def estimate(self, instance_type: str, duration: int = 3600):
        result = self.orchestrator.estimate_payment(
            duration=duration, 
            instance_type=instance_type,
        )
        logging.info(result)

if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv()

    appr = ApproveAllowance()
    appr.approve()
    appr.get_allowance()
    # appr.estimate(instance_type='C1ae.medium', duration=3600)