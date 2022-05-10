# Python-SQS-S3-automation
1 - creating 2 s3 buckets one to download from and second one to upload to 
2 - creating sqs standard that notified when s3 has new uploaded object
3 - python script that check sqs notification and notification only of 'aws:s3'
4 - if this notification found , python script download objects from first s3 bucket then upload it to second s3 bucket then delete notification from sqs to avoid downloding and uploading each again , only if new notification 'new upload' founded. 
5 - before run python code install boto3 by 
    # pip install boto3 
6- needs a customized policy of send message on sqs 
7- needs to add a notification on first bucket to my sqs 
