import pymongo
import datetime
import pandas as pd
import dns

class Database:
    def connectionString(database, collection):
        '''
        Connection string to NoSQL AtlasDB
        '''
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://Intov8-IOTAdmin:Honda08@cluster0.uijmw.mongodb.net/WaterTankIOT?retryWrites=true&w=majority")
            database = client[str(database)]
            collection = database[str(collection)]
            return collection
        except:
            print('Unable to connect to MongoDB Atlas Database, please review connection string and try again')

    def insertReadingData(readingDateTime,reading,tank,collection):
        '''
        Insert records
        '''
        record = {"readingDateTime": readingDateTime, "reading": reading, "tank": tank}
        collection.insert_one(record)

    def insertNewTankData(tank,height,capacity,usableCapacity,collection):
        '''
        Insert new Tank
        '''
        record = {"tank": tank, "height": height, "capacity" : capacity, "usableCapacity": useableCapacity}
        collection.insert_one(record) 

    def queryTankData(tank,readingDateTime,collection):
        '''
        Query database: Utilises list to convert cursor into json data
        '''
        results =  collection.find({"tank": tank, "readingDateTime": readingDateTime})
        dataframe = pd.DataFrame.from_records(list(results))
        return dataframe
        