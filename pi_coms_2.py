import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()

while True:
    try:
        readStr = ser.readline()
        #print(readStr)
        readJson = json.loads(readStr)
        #print(readJson)
        dist = readJson["range"]
        imu = readJson["imu"]
        roll = imu[0]
        pitch = imu[1]
        yaw = imu[2]
        print(dist,roll,pitch,yaw,)
    except:
        print("not valid json") #This usually only happens once at the start
        pass
      
