import serial as serial  # Import Serial Library
# Import all the vPython library
from vpython import *
import pyttsx3
engine = pyttsx3.init()
# Create an object for the Serial port. Adjust 'com11' to whatever port your arduino is sending to.
arduinoSerialData = serial.Serial('com4', 9600)

measuringRod = cylinder(title="My Meter", radius=.5,
                        length=6, color=color.yellow, pos=vector(-3, 0, 0))
lengthLabel = label(
    pos=vector(0, 1, 0), text='Target Distance is: ',  height=30)
target = box(pos=vector(0, -.5, 0), length=.2,
             width=3, height=3, color=color.green)
while (1 == 1):  # Create a loop that continues to read and display the data
    rate(20)  # Tell vpython to run this loop 20 times a second
    # Check to see if a data point is available on the serial port
    if (arduinoSerialData.inWaiting() > 0):
        myData = arduinoSerialData.readline()  # Read the distance measure as a string
        distance = float(myData)  # convert reading to a floating point number
        if distance < 5:
            engine.say("fuck off")
            engine.runAndWait()
        # print(distance)
        # Change the length of your measuring rod to your last measurement
        measuringRod.length = distance
        target.pos = vector(-3+distance, -.5, 0)
        # Create label by appending string myData to string
        myLabel = 'Target Distance is: ' + str(distance)
        lengthLabel.text = myLabel  # display updated myLabel on your graphic
