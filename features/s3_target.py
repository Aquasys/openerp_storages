from lettuce import *
import boto

@step('When I click on "save"')
def store_connection_informations(step, url, bucket, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
	world.url = url
	world.bucket = bucket
	world.AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
	world.AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY

@step('I click on "test connection"')
def test_connection(step):
	try:
		conn = boto.connect_s3(world.AWS_ACCESS_KEY_ID, world.AWS_ACCESS_KEY_ID)
		conn.get_bucket(world.bucket)
	except e:
		return -1
	return 1
