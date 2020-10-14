import pymongo
import datetime
import pandas as pd
import dns

class Database:
    def __init__(self,database=None,collection=None,readingDateTime=None,reading=None,tank=None):
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

    def queryTankData(self):
        '''
        Query database: Utilises list to convert cursor into json data
        '''
        results =  self.collection.find({"tank": self.tank, "readingDateTime": self.readingDateTime})
        dataframe = pd.DataFrame.from_records(list(results))
        return dataframe
        
class Tank:
    def __init__(self,tank,collection,height=None,diameter=None,capacity=None,usableCapacity=None, reading=None):
        '''
        innit constructor
        '''
        self.tank = tank
        self.collection = collection
        self.height = height
        self.diameter = diameter
        self.capacity = capacity 
        self.usableCapacity = usableCapacity
        self.reading = reading

    def insertNewTankData(self):
        '''
        Insert new Tank
        '''
        record = {"tank": self.tank, "height": self.height,"diameter": self.diameter, "capacity" : self.capacity, "usableCapacity": self.usableCapacity}
        self.collection.insert_one(record) 

    def tankDimensions(self):
        '''
        Returns tank dimensions
        '''
        results = self.collection.find({"tank": self.tank})
        dataframe = pd.DataFrame.from_records(list(results))
        return dataframe

    def calcPercentFull(self):
        '''
        Calculates percent full of tank
        '''
        a = 3.14*(self.diameter/2)**2*self.reading
        b = 3.14*(self.diameter/2)**2*self.height
        c = a/b
        return c


