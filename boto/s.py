import boto.ec2
boto.set_stream_logger('boto')
conn = boto.ec2.connect_to_region('us-west-2')
type(conn)

conn = boto.ec2.connect_to_region('us-west-2',
    aws_access_key_id = 'AKTAT34R4CELIXMA3IYQ',
    aws_secret_access_key = 'otv9xfde/PMu5SG5A+ttKxdAM4QPWh9OIP7p8qoR')

conn.APIVersion

conn.stop_instances(instance_ids=['i-0c63c31167651d9c9'])

#key = s3.get_bucket('media.yourdomain.com').get_key('examples/first_file.csv')
#key.get_contents_to_filename('/myfile.csv')


import boto3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
        print(bucket.name)

