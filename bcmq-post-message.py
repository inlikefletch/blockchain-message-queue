import boto3,time,sys,random
def lambda_handler(event, context):
    
    #get event
    toUserMd5 = event['to']
    message = event['message']
    
    #timestamp and random hex
    #timestamp = time.strftime("%Y%m%d%H%M%S", time.gmtime())
    daystamp = time.strftime("%Y%m%d", time.gmtime())
    #randomHex = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    
    #get count id
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
        except: x = 1
    
    #post message
    response = client.put_object(
        ACL='private',
        Body=message,
        Bucket='bcmq.tk',
        ContentType='html',
        Key='messages/'+toUserMd5+'/'+daystamp+'-'+str(count)
    )
    print response
    return 'successfulMessagePost'
