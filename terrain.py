from lettuce import world
from lettuceterrain import set_root_url


set_root_url('http://127.0.0.1:8000')

# Define global variables
# FIXME is it really needed ? Shouldn't it go in an example ?
world.url = ""
world.bucket = ""
world.AWS_ACCESS_KEY_ID = ""
world.AWS_SECRET_ACCESS_KEY = ""
