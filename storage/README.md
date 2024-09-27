[![PyPI version](https://img.shields.io/pypi/v/python-mcs-sdk)](https://pypi.org/project/python-mcs-sdk/)
# Swan MultiChain Storage SDK Samples

This directory contains samples for Swan MultiChain Storage System. Swan MultiChain Storage is the Web3 cloud computing solution for storage bucket creation, deployment and management. User can create and manage buckets through samples under this directory. For more information checkout [Swan MCS Developer Docs](https://docs.filswan.com/).

## Setup

### Authentication (API Key)

This sample (and Swan SDK) requires you to have API Key from MCS.

Steps to get a MCS API Key:

- Go to [Multi Chain Storage](https://www.multichain.storage/home). Make sure you're under the Mainnet environment.
- Login through MetaMask.
- Click the gear icon on the top right and select 'Setting'.
- Click 'Create API Key'
- Store your API Key safely, do not share with others.


### Install Dependencies
1. Clone the python-sdk-docs-samples.

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

### Store Your Environment Variables Securely 
Python-dotenv is recommended to be used to store environment variables safely. (Contained within requirements.txt)
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

    MCS API key will be required for using Swan Storage APIs.
```txt
MCS_API_KEY = <your_storage_api_key>
```
4. Load your personal information (Optional)
We recommand storing personal information as environment variables for safety.
```python
from dotenv import load_dotenv
load_dotenv()

import os

API_KEY = os.get("MCS_API_KEY")
```

## Run Samples

### Create and Delete a Bucket
Create and delete a bucket.
```bash
$ python storage/create_delete_bucket.py
```

### Get Bucket information
Retrieve information for a single bucket but also for all buckets.
```bash
$ python storage/info_bucket.py
```

### Create and Upload Folders to a Bucket
Detailed breakdown of how to create folders and upload MCS and IPFS folders.
```bash
$ python storage/folders_bucket.py
```

### Upload, Download, and Delete a file in a Bucket
Detailed breakdown of how to upload, download, and delete a file in a Bucket.
```bash
$ python storage/file_bucket.py
```

### Get info of files in a Bucket
Retrieve information on a particular file or all files in a Bucket.
```bash
$ python storage/file_info_bucket.py
```

