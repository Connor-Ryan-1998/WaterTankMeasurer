import pymongo
import datetime
import pandas as pd


def connect(database, collection):
    '''
    Connection string
    '''
    client = pymongo.MongoClient(
        "mongodb+srv://Cloud-ConnectAdmin:Password1@cluster0.zb1jw.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
    database = client[str(database)]
    collection = database[str(collection)]
    return collection
    #query = {"user": "Connor"}
    #records = collection.find(query)
    #df = pd.DataFrame(list(records))
    #x = df["Capacity"]
    # return x
# record = {"date": datetime.datetime.now(), "value": "140", "user": "Connor",
#           "Height": "1500", "Capacity": "200"}


print(connect("CloudTest", "Data"))


def checkIn(self):
    pass
