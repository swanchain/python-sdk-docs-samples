import logging
import os
from dotenv import load_dotenv
from swan_mcs import APIClient, BucketAPI



def bucket_file(bucket_client: BucketAPI, bucket_name, object_name: str, file_path: str) -> None:
   
    # create a bucket and store the function return
    bucket_create_success = bucket_client.create_bucket(bucket_name)

    # exit if the bucket can not be created
    if not bucket_create_success:
        logging.info(f"Error creating bucket: {bucket_name}")
        exit()


    # upload the file to the bucket
    file_upload_status = bucket_client.upload_file(bucket_name, object_name, file_path)
    logging.info(file_upload_status.to_json())


    # download the file
    local_object_name= "my-local-file-name"
    file_download_status = bucket_client.download_file(bucket_name, object_name, local_object_name)
    if not file_download_status:
        logging.info(f"Error downloading file: {object_name}")


    # delete the file
    file_delete_status = bucket_client.delete_file(bucket_name, object_name)
    if not file_delete_status:
        logging.info(f"Error deleting file: {object_name}")



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
    
    # you can spicifiy the folder path that the file fill be uploaded to in the bucket
    object_name = "folder1/my-test-file"
    file_path = "log_mcs.png"
    bucket_name = "my-test-bucket"
    bucket_file(bucket_client, bucket_name, object_name, file_path)