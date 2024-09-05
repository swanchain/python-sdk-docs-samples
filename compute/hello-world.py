import os
import time
import dotenv
import swan
import logging
import asyncio
import aiohttp

class HelloWorld:
    def __init__(self):
        self.orchestrator = swan.resource(
            api_key=os.getenv("SWAN_API_KEY"), 
            network='mainnet',
            service_name='Orchestrator'
        )
            
    def deploy(self):
        result = self.orchestrator.create_task(
            repo_uri='https://github.com/swanchain/awesome-swanchain/tree/main/hello_world',
            wallet_address=os.getenv("WALLET_ADDRESS"),
            private_key=os.getenv("PRIVATE_KEY"),
            instance_type='C1ae.small',
            auto_pay=True
        )
        self.task_uuid = result['task_uuid']
        task_info = self.orchestrator.get_deployment_info(task_uuid=self.task_uuid)
        logging.info(task_info)

    def wait_for_running(self):
        # wait for app URLs be generated
        app_urls = []
        while True:
            time.sleep(5)
            if app_urls := self.orchestrator.get_real_url(task_uuid=self.task_uuid):
                logging.info(f"App will be running at {app_urls}")
                break
        
        # wait for app to be running
        async def wait_for_url(url):
            start_time = time.time()
            async with aiohttp.ClientSession() as session:
                # after 5 minutes, assume app url is not running
                while time.time() - start_time < 300:
                    async with session.get(url) as resp:
                        if resp.status == 200:
                            logging.info(f"App is running at {url}")
                            logging.info(f"Response: {await resp.text()}")
                            break
                        await asyncio.sleep(5)
                else:
                    logging.warning(f"App is not running at {url} after 5 minutes")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*[wait_for_url(url) for url in app_urls]))


if __name__ == "__main__":
    # Load environment variables from the .env file
    dotenv.load_dotenv("../.env")

    hello_world = HelloWorld()
    hello_world.deploy()
    hello_world.wait_for_running()