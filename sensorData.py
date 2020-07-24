# Import Serial Library
import serial as serial
# Import all the vPython library
from vpython import *
import pyttsx3
engine = pyttsx3.init()
# Create an object for the Serial port. Adjust 'com11' to whatever port your arduino is sending to.
import databaseFunctions 
arduinoSerialData = serial.Serial('com3', 9600)

# measuringRod = cylinder(title="My Meter", radius=.5,
#                         length=6, color=color.yellow, pos=vector(-3, 0, 0))
# lengthLabel = label(
#     pos=vector(0, 1, 0), text='Target Distance is: ',  height=30)
# target = box(pos=vector(0, -.5, 0), length=.2,
#              width=3, height=3, color=color.green)

# Create a loop that continues to read and display the data
while True:
    # Tell vpython to run this loop 20 times a second
    rate(20)
    #Check to see if a data point is available on the serial port
    if (arduinoSerialData.inWaiting() > 0):
        myData = arduinoSerialData.readline()  # Read the distance measure as a string
        distance = float(myData)  # convert reading to a floating point number
        print(distance)
        #Send record to database once per x time, run for 10 mins on schedule and take median?


