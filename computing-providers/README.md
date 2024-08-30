# Swan SDK Orchestrator Task Samples

This directory contains samples for Swan Orchestrator. Computing Providers informations can be retrieved using Orchestrator APIs through provided samples under this directory. For more information checkout [Swan Developer Docs](https://docs.swanchain.io/).

## Setup

### Authentication
To retrieve information from computing providers does not require Orchestrator API Keys. All the information are open to public and can be checked without authentication.

### Install Dependencies
1. Clone the python-sdk-docs-samples  and change directory to the directory you want to use.
```bash
$ git clone https://github.com/swanchain/python-sdk-docs-samples.git
```
and
```bash
$ cd computing-providers
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