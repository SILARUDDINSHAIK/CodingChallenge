# CodingChallenge

These repository had done as part of the technical assessment and consists of deploying a simple analytics
workload using AWS services.

#General flow of working
1. Git clone
2. Run the SNSTopicDataGen.py to generate analytic event json files based on problem statement
3. SNSGen.py helps to create SNS topic from which we require topic arn to publish message through lambda functions
4. Create seperate SNS Topics
5. Create lamda function under AWS Console with your user.
   Among Services under Compute section, click Lambda and then create function.
6. To publish messages to sns topic deployed lambda files as zip archieves
7. Either directly use the lambda inline function editor or use lamda console to upload deployment package of lambda functions(Eg; SnsAnalyticEvent/SnsAnalyticEvent.zip)
8. I tried two ways to ingest messages to the SNS Topics
9. One way is through calling the lamda functions after reading each message. Providing each record as a message and publishing one by one.
10.Second way is through Simple Query Service(SQS): Run SQS.py to create new SQS

11.Configure an SQS queue as an event source for our Lambda, Lambda functions are automatically triggered when messages arrive to the SQS queue.

11.Dump Json into the SQS Queue and set the batch size.

12.Lambda function will trigger automatically based on messages into SQS batch.

