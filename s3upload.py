import boto3 
import uuid
import os,sys,threading
from boto3.s3.transfer import TransferConfig

class ProgressPercentage(object):
        def __init__(self, filename):
            self._filename = filename
            self._size = float(os.path.getsize(filename))
            self._seen_so_far = 0
            self._lock = threading.Lock()

        def __call__(self, bytes_amount):
            # To simplify we'll assume this is hooked up
            # to a single filename.
            with self._lock:
                self._seen_so_far += bytes_amount
                percentage = (self._seen_so_far / self._size) * 100
                sys.stdout.write(
                    "\r%s  %s / %s  (%.2f%%)" % (
                        self._filename, self._seen_so_far, self._size,
                        percentage))
                sys.stdout.flush()

def upload(file,token):
    ACCESS_KEY = 'AKIASW5B232QZWDDSIUZ'
    SECRET_KEY = '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'
    config = TransferConfig(multipart_threshold=1024*25, max_concurrency=10,
                        multipart_chunksize=1024*25, use_threads=True)
    with open(file, "rb") as videoFile:
        s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
        bucket = s3.Bucket(name="semi-live")
        filename = str(uuid.uuid4())
        filename = "development/"+ filename + ".mp4"
        bucket.upload_fileobj(videoFile,filename,ExtraArgs={'ACL': 'public-read',"ContentType":"video/mp4"},Config = config,Callback=ProgressPercentage(file))
    fileLink="https://semi-live.s3.us-east-2.amazonaws.com/"+filename
    return fileLink

