from lettuce import *
from lettuceterrain.terrain import *
import boto

@step('When I click on button "save"')
def store_connection_informations(step, url, bucket, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    world.url = url
    world.bucket = bucket
    world.AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
    world.AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY