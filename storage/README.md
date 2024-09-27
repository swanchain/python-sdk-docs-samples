[![PyPI version](https://img.shields.io/pypi/v/python-mcs-sdk)](https://pypi.org/project/python-mcs-sdk/)
# Swan MultiChain Storage SDK Samples <!-- omit in toc -->

This directory contains samples for Swan MultiChain Storage System. Swan MultiChain Storage is the Web3 cloud computing solution for storage bucket creation, deployment and management. User can create and manage buckets through samples under this directory. For more information checkout [Swan MCS Developer Docs](https://docs.swanchain.io/bulders/tools/multi-chain-storage).

- [Setup](#setup)
  - [Authentication (API Key)](#authentication-api-key)
  - [Install Dependencies](#install-dependencies)
  - [Store API Key in .env](#store-api-key-in-env)
- [Run Samples](#run-samples)
  - [Create and Delete a Bucket](#create-and-delete-a-bucket)
  - [Get Bucket information](#get-bucket-information)
  - [Create and Upload Folders to a Bucket](#create-and-upload-folders-to-a-bucket)
  - [Upload, Download, and Delete a file in a Bucket](#upload-download-and-delete-a-file-in-a-bucket)
  - [Get info of files in a Bucket](#get-info-of-files-in-a-bucket)


## Setup

### Authentication (API Key)

To use the `swan-sdk` Multi-Chain Storage (MCS) service, an MCS API key is required. To get an MCS API Key: visit [MultiChain Storage](https://www.multichain.storage/home).


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

### Store API Key in .env

1. Create a new .env file
2. Store your MCS API key in .env file:
```txt
MCS_API_KEY = <your_storage_api_key>
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

