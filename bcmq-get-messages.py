import boto3,time
def lambda_handler(event, context):
    
    #get event
    toUserMd5 = event['to']
    print toUserMd5
    
    #daystamp
    daystamp = time.strftime("%Y%m%d", time.gmtime())
    
    #get messages
    messages = []
    count = 0
    x = 0
    client = boto3.client('s3')
    while x != 1:
        count += 1
        try:
            response = client.get_object(
                Bucket='bcmq.tk',
                Key='messages/'+toUserMd5+'/'+daystamp+'-'+str(count)
            )
            print response
            messages.append(response['Body'].read())
        except: x = 1
    print messages
    return messages
