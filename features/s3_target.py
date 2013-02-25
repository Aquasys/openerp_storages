from lettuce import *
import boto

@step('Store connection information to external storage s3')
def store_connection_informations(step, url, bucket, AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID):
	world.url = url
	world.bucket = bucket
	world.AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
	world.AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID

@step('I click on "test connection"')
def test_connection(step):
	try:
		conn = boto.connect_s3(world.AWS_ACCESS_KEY_ID, world.AWS_ACCESS_KEY_ID)
		conn.get_bucket(world.bucket)
	Exception e:
		return -1
	return 1
