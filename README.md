[![PyPI version](https://img.shields.io/pypi/v/swan-sdk)](https://pypi.org/project/swan-sdk/)
# Python SDK Docs Samples <!-- omit in toc -->

Python samples for the [Swan SDK](https://github.com/swanchain/python-swan-sdk)

- [Setup](#setup)
- [How to run a sample](#how-to-run-a-sample)
- [References](#references)


## Setup

1. Clone the repository

```bash

git clone https://github.com/swanchain/python-sdk-docs-samples.git

```

2. Obtain authentication credentials.

To use `swan-sdk`, an Swan API Key is required.

Steps to get an Swan API Key:

- Go to [Swan Console](https://console.swanchain.io/api-keys). Make sure you're under the Mainnet environment.
- Login through MetaMask.
- Click 'Generate API Key'.
- Store your API Key safely, do not share with others.

To use the `swan-sdk` Multi-Chain Storage (MCS) service, an MCS API key is required.

Steps to get a MCS API Key:

- Go to [Multi Chain Storage](https://www.multichain.storage/home). Make sure you're under the Mainnet environment.
- Login through MetaMask.
- Click the gear icon on the top right and select 'Setting'.
- Click 'Create API Key'.
- Store your API Key safely, do not share with others.


3. Set up environment variables
   Create a `.env` file in the root directory and add the following environment variables:

```bash
WALLET_ADDRESS=<your_wallet_address>
PRIVATE_KEY=<your_private_key>
SWAN_API_KEY=<your_swanchain_api_key>
MCS_API_KEY=<your_mcs_api_key>
```

Make sure to replace the placeholders with your actual values.
And have enough balance in your wallet to run the test.

## How to run a sample

1. Set Up the Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the sample:

```bash
python compute/<sample_name>.py
python storage/<sample_name>.py
```

- for `compute` example details, checkout the [document](compute/README.md)
- for `storage` example details, checkout the [document](storage/README.md)


## References
https://github.com/GoogleCloudPlatform/python-docs-samples
