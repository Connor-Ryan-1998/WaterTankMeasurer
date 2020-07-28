import databaseFunctions as df
import datetime
#Connection String
collection = df.Database(database="WaterTankIOT", collection="dbo.waterTankReadings").connectionString()
collection.delete_many({})
