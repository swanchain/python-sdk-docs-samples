import logging
import os
from dotenv import load_dotenv
from swan_mcs import APIClient, BucketAPI

def bucket_info(bucket_client: BucketAPI, bucket_names: list[str]) -> None:
    # create buckets and store the function returns as a tuple of the bucket name and creation status
    bucket_create_statuses = [(bucket_name, bucket_client.create_bucket(bucket_name)) for bucket_name in bucket_names]

    # Determine which bucket could not be created
    for bucket_create_status in bucket_create_statuses:
        if not bucket_create_status[1]:
            logging.info(f"Error creating bucket: {bucket_create_status[0]}")

    # get the buckets that were created
    created_buckets = [bucket_create_status[0] for bucket_create_status in bucket_create_statuses if bucket_create_status[1]]


    # exit if no buckets were created
    if not created_buckets:
        exit()


    # get the info of the first created bucket
    logging.info(bucket_client.get_bucket(created_buckets[0]).to_json())

    # get the info of all the buckets
    for i in bucket_client.list_buckets():
        logging.info(i.to_json())


    # delete the buckets
    bucket_delete_statuses = [(bucket_name, bucket_client.delete_bucket(bucket_name)) for bucket_name in created_buckets]

    # Determine which bucket could not be deleted
    for bucket_delete_status in bucket_delete_statuses:
        if not bucket_create_status[1]:
            logging.info(f"Error deleting bucket: {bucket_create_status[0]}")



if __name__ == '__main__':
    load_dotenv("../.env")

    # create the bucket client
    API_KEY = os.get("API_KEY")
    ACCESS_TOKEN = os.get("ACCESS_TOKEN")
    CHAIN_NAME = os.get("CHAIN_NAME")
    mcs_api = APIClient(API_KEY, ACCESS_TOKEN, CHAIN_NAME)
    bucket_client = BucketAPI(mcs_api)

    # define the names of the bucket to be created
    bucket_names = ["my-test-bucket-1", "my-test-bucket-2"]
    bucket_info(bucket_client, bucket_names)

