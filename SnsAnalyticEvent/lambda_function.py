from venv import logger
import boto3
from botocore.exceptions import ClientError

''' AWS Console: Under services compute section create following lambda functions'''
'''User must have necessary permissions to publish messages to sns topic'''

def SnsAnalyticEvent(event, context, message):
    client = boto3.client('sns')
    try:
       response = client.publish(
          TargetArn="<ARN of the SNS topic>",
          Message=message,
          MessageStructure='json'
       )
       message_id = response['MessageId']
       logger.info("Published first sns analytic event message to topic")
    except ClientError:
       logger.exception("Couldn't publish message to topic")
       raise
    else:
       return message_id

for src_file in ['Data/FirstSnsData.json']:
  with open(src_file, 'r') as json_file:
    for message in json_file:
        SnsAnalyticEvent(event, context, message)
