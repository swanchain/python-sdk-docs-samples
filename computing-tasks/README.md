# Swan SDK Orchestrator Task Samples

This directory contains samples for Swan Orchestrator. Swan Orchestrator is the Web3 cloud computing solution for tasks creation, deployment and management. For more information checkout [Swan Developer Docs](https://docs.swanchain.io/).

## Setup

### Authentication (API Key)

This sample (and Swan SDK) requires you to have API Key from Swan Orchestrator.

Steps to get an API Key:

- Go to [Orchestrator Dashboard](https://orchestrator.swanchain.io/provider-status), switch network to Mainnet.
- Login through MetaMask.
- Click the user icon on the top right.
- Click 'Show API-Key' -> 'New API Key'
- Store your API Key safely, do not share with others.

### Install Dependencies
1. Clone the python-sdk-docs-samples  and change directory to the directory you want to use.
```bash
$ git clone https://github.com/swanchain/python-sdk-docs-samples.git
```
2. Install and updgrade pip and virtualenv if you do not already have them.
3. Create virtualenv compatible with Python 3.7+
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
4. Install the dependencies from the requirements file
```bash
$ pip install -r requirements.txt
```

### Store Your Environmental Variables Securely 
Python-dotenv is recommended to be used to store environmental variables safely. (Contained within requirements.txt)
1. Install python-dotenv (if you have not)
```bash
$ pip install python-dotenv
```
or
```bash
$ pip install -r requirements.txt
```
2. Create a new .env file
```bash
$ sudo vim .env
```
3. Store your personal information
public address will be required for authorization on Swan Orchestrator. \
private address will be required for signing onchain transactions. \
API key will be required for using Swan Orchestrator APIs.
```txt
WALLET_ADDRESS=<your_wallet_address>
PRIVATE_KEY=<your_private_key>
SWAN_API_KEY=<your_swanchain_api_key>
```
4. Load your personal information
```python

```

## Run Samples