import os
from dotenv import load_dotenv
import swan


def bucket_folders(bucket_client: swan.BucketAPI, bucket_name: str) -> None:
    """Create the different types of folders

    Args:
        bucket_client: The BucketApi client to use MultiChain Storage.
        bucket_name: The name of the bucket.

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
        print(f"Error creating bucket: {bucket_name}")
        return

    # create a folder
    # If you want to place the folder directly in the root directory, you can leave the prefix field empty
    folder_name = "my-test-folder"
    create_folder_status = bucket_client.create_folder(bucket_name, folder_name, prefix='my-test-prefix')
    if not create_folder_status:
        print(f"Failed to create folder: {folder_name}")


    # upload a MCS folder under bucket_name/object_name and print the info of the files in the folder that were uploaded
    object_name = "my-mcs-test-object"
    mcs_folder_path = "res/my-mcs-test-folder"
    mcs_folder_upload_status = bucket_client.upload_folder(bucket_name, object_name, mcs_folder_path)
    print("MCS folder file information:")
    for file_info in mcs_folder_upload_status:
        print(file_info.to_json())


    # upload an IPFS folder under bucket_name/object_name and print the info of the files in the folder that were uploaded
    object_name = "my-ipfs-test-object"
    ipfs_folder_path = "res/my-ipfs-test-folder"
    ipfs_folder_upload_info= bucket_client.upload_ipfs_folder(bucket_name, object_name, ipfs_folder_path)
    print("IPFS folder information:")
    print(ipfs_folder_upload_info.to_json())

    # delete the bucket
    bucket_delete_success = bucket_client.delete_bucket(bucket_name)

    # print error if the bucket could not be deleted
    if not bucket_delete_success:
        print(f"Error deleting bucket: {bucket_name}")


if __name__ == '__main__':
    # load environment variables
    load_dotenv()

    # create the bucket client
    API_KEY = os.getenv("MCS_API_KEY")
    # set is_calibration=True if using the calibration MCS
    bucket_client = swan.resource(api_key=API_KEY, service_name='storage')

    bucket_name = "my-test-bucket"
    bucket_folders(bucket_client, bucket_name)