import os
import pymongo
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_CLIENT = os.environ.get("MONGO_CLIENT")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLLECTION_METERS = os.environ.get("MONGO_COLLECTION_METERS")
MONGO_COLLECTION_CHANNELS = os.environ.get("MONGO_COLLECTION_CHANNELS")
MONGO_COLLECTION_GROUPS = os.environ.get("MONGO_COLLECTION_GROUPS")
client = pymongo.MongoClient(MONGO_CLIENT)
db = client[MONGO_DB]
meters_collection = db[MONGO_COLLECTION_METERS]
channels_collection = db[MONGO_COLLECTION_CHANNELS]
groups_collection = db[MONGO_COLLECTION_GROUPS]
