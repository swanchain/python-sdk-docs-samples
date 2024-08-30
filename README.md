# Python SDK Docs Samples

Python samples for the [Swan SDK](https://github.com/swanchain/python-swan-sdk)

## Setup

1. Install [`pip` and `virtualenv`][cloud_python_setup] if you do not already have them
2. Clone the repository

```bash

git clone https://github.com/swanchain/python-sdk-docs-samples.git

```

3. Obtain authentication credentials.
   To use `swan-sdk`, an Orchestrator API key is required.

- Go to [Orchestrator Dashboard](https://orchestrator.swanchain.io/provider-status), switch network to Mainnet.
- Login through MetaMask.
- Click the user icon on the top right.
- Click 'Show API-Key' -> 'New API Key'

4. Set up environment variables
   Create a `.env` file in the root directory and add the following environment variables:

```bash
WALLET_ADDRESS=<your_wallet_address>
PRIVATE_KEY=<your_private_key>
SWAN_API_KEY=<your_swanchain_api_key>
```

Make sure to replace the placeholders with your actual values.
And have enough balance in your wallet to run the test.

## How to run a sample

1. Change directory to one of the sample folders, e.g. cd `compute`

```bash
cd compute 
```

2. Set Up the Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the sample:

```bash
python -m pytest -s  <test_file_name>.py
```


## References
https://github.com/GoogleCloudPlatform/python-docs-samples
