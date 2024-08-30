# Swan SDK Orchestrator Task Samples

This directory contains samples for Swan Orchestrator smart contracts. Samples for Swan Token and Swan Payment Contract are under this directory. For more information checkout [Swan Developer Docs](https://docs.swanchain.io/).

## Setup

### Authentication
User need to have Web3 wallet to interact with Swan Smart Contracts. Recommanded wallet for broswer usage is [MetaMask](https://metamask.io/).

### Install Dependencies
1. Clone the python-sdk-docs-samples  and change directory to the directory you want to use.
```bash
$ git clone https://github.com/swanchain/python-sdk-docs-samples.git
```
and
```bash
$ cd swan-contract
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

## Run Samples