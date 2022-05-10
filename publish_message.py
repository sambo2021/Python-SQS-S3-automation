import boto3
import json
import env
import os
from receive_message import receive_message
from delete_message import delete_message
"""
check sqs notification
"""
sqs_url = env.sqs_url
max_number_of_messages = 1
wait_time_seconds = 20
region = env.region
response = receive_message(sqs_url, max_number_of_messages, wait_time_seconds, region)
messages_list = response.get('Messages', [])
print(f"Number of messages received: {len(messages_list)}")
check = False
for message in messages_list:
   message_body_str = message["Body"]
   message_body_dict = json.loads(message_body_str)
   check = message_body_dict['Records'][0]['eventSource']
print(check)
if check=='aws:s3':
      """
      connect ro s3 services 
      """
      client_s3 = boto3.client(
         's3',
         region,
         aws_access_key_id=env.accessKey,
         aws_secret_access_key=env.secretKey,
      )
      data_file_folder = os.path.join(os.getcwd(),'data Files')
      """
      download files from bucket_a
      """
      s3 = boto3.resource('s3')
      for s3_object in s3.Bucket(env.bucket_a).objects.all():
         filename = s3_object.key
         client_s3.download_file(env.bucket_a,s3_object.key,os.path.join(data_file_folder, filename))
      """
      upload files to bucket_b
      """
      for file in os.listdir(data_file_folder):
         print('Uploading file {0} ...'.format(file))
         client_s3.upload_file(
            os.path.join(data_file_folder, file),
            env.bucket_b,
            file
         )
      """
      Delete Message Example 
      """
      max_number_of_messages = 5
      wait_time_seconds = 20
      response = receive_message(sqs_url, max_number_of_messages, wait_time_seconds, region)
      messages_list = response.get('Messages', [])
      # Deleteing certain message
      for message in messages_list:
        message_body_str = message["Body"]
        message_body_dict = json.loads(message_body_str)
        receipt_handle = message['ReceiptHandle']
        response = delete_message(sqs_url, receipt_handle, region)
        print(response)
else:
      print("there is no uploaded files on s3 , invalid resource")
