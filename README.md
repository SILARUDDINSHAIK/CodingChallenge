# CodingChallenge

These repository had done as part of the technical assessment and consists of deploying a simple analytics
workload using AWS services.

#General flow of working
1. Git clone
2. Run the SNSTopicDataGen.py to generate analytic event json files based on problem statement
3. SNSGen.py helps to create SNS topic from which we require topic arn to publish message through lambda functions
4. 
