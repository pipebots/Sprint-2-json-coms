import serial
import json

port = "/dev/ttyACM0"

s1 = serial.Serial(port,9600)
s1.flushImput()

while True:
    listenJSON()

def listenJSON():
    if s1.inWaiting()>0:
        inputValue =s1.readline() # need to define how much to read here using read(x) or will readline do it?
        print(inputValue)
        vals = json.loads(inputValue)
        range = vals["range"]
        imu = vals["imu"]
        roll = imu[0]
        pitch = imu[1]
        yaw = imu[2]
        
