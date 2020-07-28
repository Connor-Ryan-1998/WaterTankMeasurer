import pymongo
import datetime
import pandas as pd
import dns

class Database:
    def __init__(self,database=None,collection=None,readingDateTime=None,reading=None,tank=None,height=None,capacity=None,usableCapacity=None):
        '''
        innit constructor
        '''
        self.database = database
        self.collection = collection
        self.readingDateTime = readingDateTime
        self.reading = reading
        self.tank = tank


    def connectionString(self):
        '''
        Connection string to NoSQL AtlasDB
        '''
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://Intov8-IOTAdmin:Honda08@cluster0.uijmw.mongodb.net/WaterTankIOT?retryWrites=true&w=majority")
            database = client[str(self.database)]
            collection = database[str(self.collection)]
            return collection
        except:
            print('Unable to connect to MongoDB Atlas Database, please review connection string and try again')

    def insertReadingData(self):
        '''
        Insert records
        '''
        record = {"readingDateTime": self.readingDateTime, "reading": self.reading, "tank": self.tank}
        self.collection.insert_one(record)

    def insertNewTankData(self):
        '''
        Insert new Tank
        '''
        record = {"tank": self.tank, "height": self.height, "capacity" : self.capacity, "usableCapacity": self.useableCapacity}
        self.collection.insert_one(record) 

    def queryTankData(self):
        '''
        Query database: Utilises list to convert cursor into json data
        '''
        results =  self.collection.find({"tank": self.tank, "readingDateTime": self.readingDateTime})
        dataframe = pd.DataFrame.from_records(list(results))
        return dataframe
        