import boto3

resource_s3 = boto3.client('s3')
resource_s3.create_bucket(
    Bucket = 'bucket-shaivin',
    CreateBucketConfiguration = {
        'LocationConstraint' : 'ap-south-1'
    }
)

bucket_list = resource_s3.list_buckets()
#print(bucket_list)

bucket_name = bucket_list['Buckets'][0]['Name']
print(f"Buckets in S3: {bucket_name}")

files = resource_s3.upload_file("/home/shaivin-sagar/Pictures/zoro.jpeg", "bucket-shaivin", "Zoro-Wallpaper")

object_list = resource_s3.list_objects(
    Bucket = bucket_name 
)
#print(object_list)

object_name = object_list['Contents'][0]['Key']
print(f"Objects in S3: {object_name}")

