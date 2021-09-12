from os import getenv as env


API_URL = env('API_URL')

BOT_TOKEN = env('BOT_TOKEN')
BOT_ADMINS = "".join(env('BOT_ADMINS').split()).split(',')

BQ_DATASET = env('BQ_DATASET')
BQ_TABLE = env('BQ_TABLE')