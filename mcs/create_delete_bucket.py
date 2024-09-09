import logging
import os
from dotenv import load_dotenv
from swan_mcs import APIClient, BucketAPI

def bucket_create_delete(bucket_client: BucketAPI, bucket_name: str) -> None:

    # create a bucket and store the function return
    bucket_create_success = bucket_client.create_bucket(bucket_name)

    # exit if the bucket can not be created
    if not bucket_create_success:
        logging.info(f"Error creating bucket: {bucket_name}")
        exit()


    # delete the bucket
    bucket_delete_success = bucket_client.delete_bucket(bucket_name)

    # print error if the bucket could not be deleted
    if not bucket_delete_success:
        logging.info(f"Error deleting bucket:{bucket_name}")


if __name__ == '__main__':
    load_dotenv("../.env")

    # create the bucket client
    API_KEY = os.get("API_KEY")
    ACCESS_TOKEN = os.get("ACCESS_TOKEN")
    CHAIN_NAME = os.get("CHAIN_NAME")
    mcs_api = APIClient(API_KEY, ACCESS_TOKEN, CHAIN_NAME)
    bucket_client = BucketAPI(mcs_api)

    bucket_name = "my-test-bucket"
    bucket_create_delete(bucket_client, bucket_name)