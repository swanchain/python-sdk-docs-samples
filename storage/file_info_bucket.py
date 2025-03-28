import os
import logging
from dotenv import load_dotenv
import swan


def bucket_file_info(bucket_client: swan.BucketAPI, bucket_name, object_name: str, file_path: str) -> None:
    """Upload files to a bucket and get info of the files

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

    # create a bucket and store the function return
    bucket_create_success = bucket_client.create_bucket(bucket_name)

    # return if the bucket can not be created
    if not bucket_create_success:
        logging.error(f"Error creating bucket: {bucket_name}")
        return


    # upload the first file to the bucket
    file_upload_status_1 = bucket_client.upload_file(bucket_name, object_name, file_path)
    logging.info("First file upload info:")
    logging.info(file_upload_status_1.to_json())

    # upload the second file to the bucket
    file_upload_status_2 = bucket_client.upload_file(bucket_name, object_name+"2" , file_path)
    logging.info("Second file upload info:")
    logging.info(file_upload_status_2.to_json())


    # git the info of a specific file
    file_info = bucket_client.get_file(bucket_name, object_name)
    logging.info("Info of a specific file:")
    logging.info(file_info.to_json())


    # get a list of files, limited to 10 only
    file_list = bucket_client.list_files(bucket_name, limit=10)
    logging.info("Info of all files in the bucket:")
    for file in file_list:
        logging.info(file.to_json())


    # delete the files
    file_delete_status_1 = bucket_client.delete_file(bucket_name, object_name)
    if not file_delete_status_1:
        logging.error(f"Error deleting file: {object_name}")

    file_delete_status_2 = bucket_client.delete_file(bucket_name, object_name+"2")
    if not file_delete_status_2:
        logging.error(f"Error deleting file: {object_name+'2'}")


    # delete the bucket
    bucket_delete_success = bucket_client.delete_bucket(bucket_name)

    # print error if the bucket could not be deleted
    if not bucket_delete_success:
        logging.error(f"Error deleting bucket:{bucket_name}")



if __name__ == '__main__':
    # load environment variables
    load_dotenv()

    # create the bucket client
    API_KEY = os.getenv("MCS_API_KEY")
    # set is_calibration=True if using the calibration MCS
    bucket_client = swan.resource(api_key=API_KEY, service_name='storage')
    
    # you can spicifiy the folder path that the file fill be uploaded to in the bucket
    object_name = "my-test-file"
    file_path = "res/logo_mcs.png"
    bucket_name = "my-test-bucket"
    bucket_file_info(bucket_client, bucket_name, object_name, file_path)