import boto
s3 = boto.connect_s3()
bucket = s3.create_bucket('media.yourdomain.com')  # bucket names must be unique
key = bucket.new_key('examples/first_file.csv')
key.set_contents_from_filename('/home/patrick/first_file.csv')
key.set_acl('public-read')