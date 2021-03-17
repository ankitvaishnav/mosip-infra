from minio import Minio

import config as conf
from utils import myPrint


class MinioWrapper:
    def __init__(self):
        myPrint(conf.minio_endpoint)
        myPrint(conf.access_key)
        myPrint("okay")
        myPrint(conf.region)
        self.client = self.createConnection()

    def createConnection(self):
        if conf.region is not None:
            return Minio(
                conf.minio_endpoint,
                access_key=conf.access_key,
                secret_key=conf.secret_key,
                region=conf.region,
            )
        else:
            return Minio(
                conf.minio_endpoint,
                conf.access_key,
                conf.secret_key
            )

    def listBuckets(self):
        return self.client.list_buckets()

    def createBucket(self, bucket_name):
        if not self.client.bucket_exists(bucket_name):
            if conf.region is not None:
                self.client.make_bucket(bucket_name)
            else:
                self.client.make_bucket(bucket_name)
        else:
            raise RuntimeError("Bucket with name "+bucket_name+" already exists")

    def bucketExists(self, bucket_name):
        if self.client.bucket_exists(bucket_name):
            return True
        else:
            return False

    def listObjects(self, bucket_name):
        return self.client.list_objects(bucket_name)

    def getObject(self, bucket_name, object_name):
        data = None
        try:
            response = self.client.get_object(bucket_name, object_name)
            data = response
        finally:
            response.close()
            response.release_conn()
        return data

    def putObject(self, bucket_name, object_name):
        return
