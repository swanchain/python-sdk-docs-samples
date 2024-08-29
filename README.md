# Python SDK Docs Samples

This is a sample test for Swan. It is a simple test that tests the basic functionality of Swan.

## Install
### Get Orchestrator API Key

To use `swan-sdk`, an Orchestrator API key is required.

- Go to [Orchestrator Dashboard](https://orchestrator.swanchain.io/provider-status), switch network to Mainnet.
- Login through MetaMask.
- Click the user icon on the top right.
- Click 'Show API-Key' -> 'New API Key'


### Install dependency
```bash
pip install -r requirements.txt
```
### Set up environment variables
Create a `.env` file in the root directory and add the following environment variables:

```bash
WALLET_ADDRESS=<your_wallet_address>
PRIVATE_KEY=<your_private_key>
SWAN_API_KEY=<your_swanchain_api_key>
```
Make sure to replace the placeholders with your actual values. 
And have enough balance in your wallet to run the test.

## Run the test
**Set Up the Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
** Run the test
```bash
python -m pytest <test_file_name>.py
```
