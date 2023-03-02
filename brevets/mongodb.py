import os
from pymongo import MongoClient


client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

db = client.brevetdb 
collection = db.brevets 

def brevet_insert(brev_dist, begin_date, checkpoints):
    data_saved = collection.insert_one({
        "brev_dist": brev_dist,
        "begin_date": begin_date,
        "checkpoints": checkpoints
    })
    _id = data_saved.inserted_id
    return str(_id)

def brevet_fetch():
    curser = collection.find().sort("_id", -1).limit(1)
    for brev_curser in curser:
        return brev_curser["brev_dist"], brev_curser["begin_date"], brev_curser["checkpoints"]
