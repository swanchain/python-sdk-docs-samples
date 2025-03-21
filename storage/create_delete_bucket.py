import os
import logging
from dotenv import load_dotenv
import swan


def bucket_create_delete(bucket_client: swan.BucketAPI, bucket_name: str) -> None:
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
        logging.error(f"Error creating bucket: {bucket_name}")
        return

    logging.info(f"Created bucket: {bucket_name}")

    # delete the bucket
    bucket_delete_success = bucket_client.delete_bucket(bucket_name)

    # print error if the bucket could not be deleted
    if not bucket_delete_success:
        logging.error(f"Error deleting bucket: {bucket_name}")
        return
    
    logging.info(f"Deleted bucket: {bucket_name}")


if __name__ == '__main__':
    # load environment variables
    load_dotenv()

    # create the bucket client
    API_KEY = os.getenv("MCS_API_KEY")
    # set is_calibration=True if using the calibration MCS
    bucket_client = swan.resource(api_key=API_KEY, service_name='storage')

    bucket_name = "my-test-bucket"
    bucket_create_delete(bucket_client, bucket_name)