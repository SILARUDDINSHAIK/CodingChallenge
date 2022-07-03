import json
import boto3

client = boto3.client('sqs')
def create_queue():
    sqs_client = boto3.client("sqs", region_name="us-west-2")
    response = sqs_client.create_queue(
        QueueName="aws-iot-event queue",
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    print(response)
    return response

def get_queue_url():
    sqs_client = boto3.client("sqs", region_name="us-west-2")
    response = sqs_client.get_queue_url(
        QueueName="aws-iot-event queue",
    )
    return response["QueueUrl"]

def send(self, Message={}):
    data = json.dumps(Message)
    response = self.queue.send_message(MessageBody=data)
    return response

#Load up the json file into the SQS Queue
for src_file in ['Data/WeeklyDiagnosticData.json']:
  with open(src_file, 'r') as json_file:
    for message in json_file:
        send(message)
