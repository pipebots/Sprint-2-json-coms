import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()

# function to read JSON doc from serial and parse variables from it
def listenJSON():
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

#function to send data formatted as JSON doc over serial
def writeJSON(int led):
    sendStr = json.dumps({'LED': led}, separators=(',',':'))
    ser.write(sendStr + "\n")

i=0
while True:
    listenJSON()
    writeJSON(i)
    i++
    if i == 10:
        i=0
