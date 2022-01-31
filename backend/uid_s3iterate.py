import boto3

def link(uid):
    ACCESS_KEY = 'AKIASW5B232QZWDDSIUZ'
    SECRET_KEY = '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'

    session = boto3.Session( 
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY)


    #Then use the session to get the resource
    s3 = session.resource('s3')

    my_bucket = s3.Bucket('semi-live')

    links = []
    folder = "development/" + uid
    flag=0
    for my_bucket_object in my_bucket.objects.filter(Prefix=folder):
        if flag==0:
            flag=1
            continue
        l = "https://semi-live.s3.us-east-2.amazonaws.com/" + str(my_bucket_object.key)
        links.append(l)
    return links

print(link("rashi4758"))    