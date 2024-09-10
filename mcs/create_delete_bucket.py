import os
from dotenv import load_dotenv
from swan_mcs import APIClient, BucketAPI


def bucket_create_delete(bucket_client: BucketAPI, bucket_name: str) -> None:
    """Create and then delete a bucket.

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
    
    # print error if the bucket can not be created
    if not bucket_create_success:
        print(f"Error creating bucket: {bucket_name}")
        return

    print(f"Created bucket: {bucket_name}")

    # delete the bucket
    bucket_delete_success = bucket_client.delete_bucket(bucket_name)

    # print error if the bucket could not be deleted
    if not bucket_delete_success:
        print(f"Error deleting bucket: {bucket_name}")
        return
    
    print(f"Deleted bucket: {bucket_name}")


if __name__ == '__main__':
    # load environment variables
    load_dotenv("../.env")

    # create the bucket client
    API_KEY = os.getenv("API_KEY")
    CHAIN_NAME = os.getenv("CHAIN_NAME")
    # set is_calibration=True if using the calibration MCS
    mcs_api = APIClient(api_key=API_KEY, chain_name=CHAIN_NAME, is_calibration=True)
    bucket_client = BucketAPI(mcs_api)

    bucket_name = "my-test-bucket"
    bucket_create_delete(bucket_client, bucket_name)