import boto3


def delete_message(queue_url, receipt_handle, region):
    sqs_client = boto3.client("sqs", region_name=region)
    response = sqs_client.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle,
    )
    return response