[![PyPI version](https://img.shields.io/pypi/v/swan-sdk)](https://pypi.org/project/swan-sdk/)
# Swan SDK Orchestrator Samples <!-- omit in toc -->

This directory contains samples for Swan Orchestrator. Swan Orchestrator is the Web3 cloud computing solution for tasks creation, deployment and management. User can create and manage tasks through samples under this directory. For more information checkout [Swan Developer Docs](https://docs.swanchain.io/).

- [Setup](#setup)
  - [Authentication (API Key)](#authentication-api-key)
  - [Install Dependencies](#install-dependencies)
  - [Store Your Environment Variables Securely](#store-your-environment-variables-securely)
- [Run Samples](#run-samples)
  - [Get Instance Resources](#get-instance-resources)
  - [Instance Configuration Example](#instance-configuration-example)
  - [Connect to Orchestrator (with Swan API Key)](#connect-to-orchestrator-with-swan-api-key)
  - [Create Task](#create-task)
  - [Renew Task / Extend Task Duration](#renew-task--extend-task-duration)
  - [Terminate Task](#terminate-task)
  - [Get Task List](#get-task-list)
  - [Get Task Deployment Info](#get-task-deployment-info)
  - [Pre-approve Payment](#pre-approve-payment)
  - [Other Examples](#other-examples)


## Setup

### Authentication (API Key)

Samples (and Swan SDK) requires you to have API Key from Swan Orchestrator.

Steps to get an API Key:

- Go to [Orchestrator Dashboard](https://orchestrator.swanchain.io/provider-status). Make sure you're under the Mainnet environment.
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

### Store Your Environment Variables Securely 

- public address will be required for authorization on Swan Orchestrator. 
- private address will be required for signing onchain transactions. 
- API key will be required for using Swan Orchestrator APIs.

```txt
WALLET_ADDRESS=<your_wallet_address>
PRIVATE_KEY=<your_private_key>
SWAN_API_KEY=<your_swan_api_key>
```


## Run Samples

### Get Instance Resources

This example shows how to retrieve all currently available CP resources online.

```bash
$ python compute/get_instance_resources.py
```

### Instance Configuration Example

This example shows detailed breakdown of instance configuration structure and usage.

```bash
$ python compute/instance_configuration_example.py
```

### Connect to Orchestrator (with Swan API Key)

This example shows how to connect to Orchestrator.

```bash
$ python compute/connect_orchestrator.py
```

### Create Task

This example shows how to create task with Swan SDK.

```bash
$ python compute/create_task.py
```

### Renew Task / Extend Task Duration

This example shows how to extend a task's duration.

Edit `task_uuid = '<task_uuid>'` in `compute/renew_task.py` to input the task_uuid you just created, and then run:

```bash
$ python compute/renew_task.py 
```

### Terminate Task

This example shows how to early terminate a task.

Edit `task_uuid = '<task_uuid>'` in `compute/terminate_task.py` to input the task_uuid which is in its duration, and then run:

```bash
$ python compute/terminate_task.py
```

### Get Task List

This example shows how to get a list of tasks under the user of API Key and wallet address.

```bash
$ python compute/get_task_list.py
```

### Get Task Deployment Info

This example shows how to get the task deployment info.

```bash
$ python compute/get_task_deployment_info.py
```

### Pre-approve Payment

This example shows how to approve an amount for payment in advance.

```bash
$ python compute/payment_approve.py
```

### Other Examples

These examples shows how to deploy specific applications.

```bash
$ python compute/hello-world.py         # hello world app
$ python compute/deploy-chainnode.py    # chainnode app
$ python compute/deploy-llama3-model.py # llama3 model app
```
