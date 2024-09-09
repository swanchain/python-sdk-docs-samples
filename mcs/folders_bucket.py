import logging
import os
from dotenv import load_dotenv
from swan_mcs import APIClient, BucketAPI


def bucket_folders(bucket_client: BucketAPI, bucket_name: str) -> None:
    # create a bucket and store the function return
    bucket_create_success = bucket_client.create_bucket(bucket_name)

    # exit if the bucket can not be created
    if not bucket_create_success:
        logging.info(f"Error creating bucket: {bucket_name}")
        exit()


    # create a folder
    # If you want to place the folder directly in the root directory, you can leave the prefix field empty
    folder_name = "my-test-folder"
    create_folder_status = bucket_client.create_folder(bucket_name, folder_name, prefix='my-test-prefix')
    if not create_folder_status:
        logging.info(f"Failed to create folder{folder_name}")


    # upload a MCS folder under bucket_name/object_name
    object_name = "my-test-object"
    mcs_folder_path = "my-test-mcs-folder_path"
    mcs_folder_upload_status = bucket_client.upload_folder(bucket_name, object_name, mcs_folder_path)
    logging.info(mcs_folder_upload_status.to_json())


    # upload an IPFS folder
    object_name = "my-test-object"
    ipfs_folder_path = "my-test-ipfs-path"
    ipfs_folder_upload_status= bucket_client.upload_ipfs_folder(bucket_name, object_name, ipfs_folder_path)
    logging.info(ipfs_folder_upload_status.to_json())

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
    bucket_folders(bucket_client, bucket_name)