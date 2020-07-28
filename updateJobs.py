import databaseFunctions as df
import datetime
import serial #Import Serial Library

#Create Serial port object called arduinoSerialData
arduinoSerialData = serial.Serial('com3',9600) 

#Connection String
collection = df.Database(database="WaterTankIOT", collection="dbo.waterTankReadings").connectionString()
while True:
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        currentDateTime = datetime.datetime.now()
        reading = [int(s) for s in myData.split() if s.isdigit()]
        df.Database(readingDateTime=currentDateTime,reading=reading[0],tank="Tank01",collection = collection).insertReadingData()
        