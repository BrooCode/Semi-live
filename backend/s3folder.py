import boto3

def makefolder(token):
    ACCESS_KEY = 'AKIASW5B232QZWDDSIUZ'
    SECRET_KEY = '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'
    s3 = boto3.client('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    bucket_name = "semi-live"
    directory_name = "development/" + token #it's name of your folders
    s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
    
