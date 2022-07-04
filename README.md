# Coding Challenge
This repository had done as a part of the technical assessment and consists of deploying a simple analytics
workload using AWS services.

### General flow of working
1. Git clone
2. Run the SNSTopicDataGen.py to generate analytic event JSON files based on the problem statement
3. SNSGen.py helps to create an SNS topic from which we require topic arn to publish message through lambda functions
4. Create separate SNS Topics
5. Create lambda function under AWS Console with your user.
   Among Services under Compute section, click Lambda and then create function.
6. To publish messages to SNS topic deployed lambda files as zip archives
7. Either directly use the lambda inline function editor or use the lambda console to upload the deployment package of lambda functions(Eg; SnsAnalyticEvent/SnsAnalyticEvent.zip)
8. I tried two ways to ingest messages to the SNS Topics
9. One way is by calling the lambda functions after reading each message. Providing each record as a message and publishing them one by one.
10. Second way is through Simple Query Service(SQS): Run SQS.py to create a new SQS

11. Configure an SQS queue as an event source for our Lambda, Lambda functions are automatically triggered when messages arrive to the SQS queue.

12. Dump Json into the SQS Queue and set the batch size.

13. Lambda function will trigger automatically based on messages into the SQS batch.


