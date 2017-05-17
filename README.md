# db-hack-aws-sns

The following documents a free database solution hack using AWS SNS as the backend. Using SNS topics as database objects allows for a free database solution. Please note, AWS SNS has a 100,000 topic limit.

The following example uses a S3 javascript object as the front end and a Lambda function as the application layer. This is a very basic authenication applicaiotn as an example. Please note I do a daily clean up of accounts at midnight UTC.

http://sns-auth.s3-website-us-west-2.amazonaws.com

Questions or comments:
jason@solvingnet.com

P.S. working on posting AWS Cloudformation templates.
