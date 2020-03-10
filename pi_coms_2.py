import serial
import json
import time

ser = serial.Serial('/dev/ttyACM0', 9600) #address when using USB cable to arduino
ser.flushInput()

# function to read JSON doc from serial and parse variables from it
def listenJSON():
    try:
        readStr = ser.readline() #doc is sent with line end termination
        #print(readStr)
        readJson = json.loads(readStr) 
        #print(readJson)
        dist = readJson["Colour"]
        imu = readJson["imu"]
        roll = imu[0]
        pitch = imu[1]
        yaw = imu[2]
        print(dist,roll,pitch,yaw,)
    except:
        print("not valid json") #At the start it is common for a partial JSON doc to be recieved and throw an error - this ignores it
        pass

#function to send data formatted as JSON doc over serial
def writeJSON(led):
    sendStr = json.dumps({'LED':led}, separators=(',',':')) + "\n"
    #print(sendStr)
    ser.write(sendStr.encode('utf-8')) #has to be encoded into bits for .write

i=0
while True:
    listenJSON()
    writeJSON(i)
    i=i+1
    if i == 8:
        i=0
    time.sleep(0.25) #so it can be seen when debugging
