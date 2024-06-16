from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.fetin
counters = db.counters


class auto_increment():
    def getNextSequence(self):
        ret = counters.find_one_and_update(
            {"_id": "cont"},
            {"$inc": {"seq": 1}},
            return_document=True
        )

        return ret['seq']