import boto3,sys,time
def lambda_handler(event, context):
    
    daystamp = time.strftime("%Y%m%d", time.gmtime())
    
    client = boto3.client('s3')
    
    #get users
    response = client.list_objects(
        Bucket='bcmq.tk',
        Prefix='users/'
    )
    results = response['Contents']
    users = []
    for result in results:
        users.append(result['Key'].split('/')[-1])
    
    #for each user, get today's messages
    blockchain = []
    for user in users:
        count = 0
        x = 0
        while x != 1:
            count += 1
            try:
                response = client.get_object(
                    Bucket='bcmq.tk',
                    Key='messages/'+user+'/'+daystamp+'-'+str(count)
                )
                print response
                blockchain.append(response['Body'].read())
            except: x = 1
    
    print blockchain
    return blockchain
