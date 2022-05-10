import boto3
def receive_message(queue_url, max_number_of_messages, wait_time_seconds, region):
    sqs_client = boto3.client("sqs", region_name=region)
    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=max_number_of_messages,
        WaitTimeSeconds=wait_time_seconds,
    )
    return response