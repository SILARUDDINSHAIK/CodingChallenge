from venv import logger
import boto3
from botocore.exceptions import ClientError

def SuccessAnalyticPayload(event, context, message):
    client = boto3.client('sns')
    try:
       response = client.publish(
          TargetArn="<ARN of the SNS topic>",
          Message=message,
          MessageStructure='json'
       )
       message_id = response['MessageId']
       logger.info("Published success Rate message to topic")
    except ClientError:
       logger.exception("Couldn't publish message to topic")
       raise
    else:
       return message_id

for src_file in ['Data/WeeklyDiagnosticData.json']:
  with open(src_file, 'r') as json_file:
    for line in json_file:
        SuccessAnalyticPayload(event, context, message)