import hashlib,binascii,os,boto3,sys,time
def lambda_handler(event, context):
    
    #get username/password/action
    usernameMd5 = event['usernameMd5']
    publicKey = event['publicKey']
    
    #get user key
    client = boto3.client('s3')
    try:
        getUser = client.get_object(
            Bucket='bcmq.tk',
            Key='users/'+usernameMd5
        )
    except: getUser = ''

    #if no user, then create public key policy object
    if getUser:
        publicKeyStore=getUser['Body'].read()
        if publicKey == publicKeyStore:
            print 'loginSuccess'
            return 'loginSuccess'
        else:
            print 'loginError'
            return 'loginError'
    elif not getUser:
        #create user public key iam policy object
        response = client.put_object(
            ACL='private',
            Body=publicKey,
            Bucket='bcmq.tk',
            ContentType='html',
            Key='users/'+usernameMd5
        )
        print response
        print 'signUpSuccess'
        return 'signUpSuccess'
    else:
        print 'auth error'
        return 'authError'
