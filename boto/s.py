#import boto.ec2
#conn = boto.ec2.connect_to_region('us-west-2c')
#conn.stop_instances(instance_ids=['i-0c63c31167651d9c9'])

#key = s3.get_bucket('media.yourdomain.com').get_key('examples/first_file.csv')
#key.get_contents_to_filename('/myfile.csv')


import boto3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
        print(bucket.name)

