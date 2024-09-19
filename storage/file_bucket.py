import os
from dotenv import load_dotenv
from swan_mcs import APIClient, BucketAPI



def bucket_file(bucket_client: BucketAPI, bucket_name, object_name: str, file_path: str) -> None:
    """Upload a file to a bucket, download the file, then delete the file

    Args:
        bucket_client: The BucketApi client to use MultiChain Storage.
        bucket_name: The name of the bucket.
        object_name: The desired file name in the bucket.
        file_path: The local path to the file.

    Return:
        None.
    """

    # try to delete the bucket, this is so that the program can run again properly if an error occurs
    # this will print an error if the bucket does not yet exist.
    bucket_client.delete_bucket(bucket_name)

    # delete the localy downloaded file if it exists
    if os.path.exists("my-downloaded-file"):
        os.remove("my-downloaded-file")
    
    # create a bucket and store the function return
    bucket_create_success = bucket_client.create_bucket(bucket_name)

    # return if the bucket can not be created
    if not bucket_create_success:
        print(f"Error creating bucket: {bucket_name}")
        return


    # upload the file to the bucket
    # replace=True will overwrite an existing file of the same name
    file_upload_status = bucket_client.upload_file(bucket_name, object_name, file_path, replace=True)
    print(file_upload_status.to_json())


    # download the file
    local_object_name= "my-downloaded-file"
    file_download_status = bucket_client.download_file(bucket_name, object_name, local_object_name)
    if not file_download_status:
        print(f"Error downloading file: {object_name}")


    # delete the file
    file_delete_status = bucket_client.delete_file(bucket_name, object_name)
    if not file_delete_status:
        print(f"Error deleting file: {object_name}")


    # delete the bucket
    bucket_delete_success = bucket_client.delete_bucket(bucket_name)

    # print error if the bucket could not be deleted
    if not bucket_delete_success:
        print(f"Error deleting bucket:{bucket_name}")




if __name__ == '__main__':
    # load environment variables
    load_dotenv("../.env")

    # create the bucket client
    API_KEY = os.getenv("API_KEY")
    CHAIN_NAME = os.getenv("CHAIN_NAME")
    # set is_calibration=True if using the calibration MCS
    mcs_api = APIClient(API_KEY, CHAIN_NAME, is_calibration=True)
    bucket_client = BucketAPI(mcs_api)
    
    # you can specify the folder path that the file will be uploaded to in the bucket
    # object name is the desired name of the file in the bucket
    object_name = "my-test-file"
    file_path = "logo_mcs.png"
    bucket_name = "my-test-bucket"
    bucket_file(bucket_client, bucket_name, object_name, file_path)