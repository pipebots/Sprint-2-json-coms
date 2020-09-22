#                                    __
#__________.__             ___.     |__|  __          
#\______   \__|_____   ____\_ |__   _||__/  |_  ______
# |     ___/  \____ \_/ __ \| __ \ /  _ \   __\/  ___/
# |    |   |  |  |_> >  ___/| \_\ (  O_O )  |  \___ \ 
# |____|   |__|   __/ \___  >___  /\____/|__| /____  >
#             |__|        \/    \/                 \/ 
# Run on pi to listen for JSON doc and parse contents, also sends JSON via serial to ardunio

import serial
import json
import time

ser = serial.Serial('/dev/ttyACM0', 9600) #address when using USB cable to arduino
ser.flushInput()

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = timestr + "-sprintbot-data.txt"
start = time.time()
# function to read JSON doc from serial and parse variables from it
def listenJSON():
    try:
        readStr = ser.readline() #doc is sent with line end termination
        #print(readStr)
        readJson = json.loads(readStr) 
        #print(readJson)
        #wheel1Pos = readJson["wheel1Pos"]
        #wheel1Revs = readJson["wheel1Revs"]
        #wheel2Pos = readJson["wheel2Pos"]
        #wheel2Revs = readJson["wheel2Revs"]
        
        #dist = readJson["Colour"]
        #imu = readJson["imu"]
        #roll = imu[0]
        #pitch = imu[1]
        #yaw = imu[2]
        #print(imu)
        #print(wheel1Pos, wheel1Revs, wheel2Pos, wheel2Revs)
        
        #timestamp = {"timestamp":time.strftime("%H %M %S")}
        timestamp = {"elapsedTime":"{:0.3f}".format(time.time()-start)}
        print(timestamp)
        #timestamp = {"timestamp":time.time}
        readJson.update(timestamp) #append timestamp to JSON file
        
        with open(filename, 'a') as outfile:
            json.dump(readJson, outfile,indent=4) #save to file
    except:
        #print(readStr)
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
    #writeJSON(i)
    i=i+1
    if i == 8:
        i=0
    time.sleep(0.25) #so it can be seen when debugging
