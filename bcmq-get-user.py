import boto3,sys
def lambda_handler(event, context):
    
    userMd5 =  event['userMd5']
    
    client = boto3.client('s3')
    try:
        response = getUser = client.get_object(
            Bucket='bcmq.tk',
            Key='users/'+userMd5
        )
        publicKey = response['Body'].read()
        print publicKey
        return publicKey
    except:
        print 'no user: ' + userMd5
        return 'userDoesNotExist'
