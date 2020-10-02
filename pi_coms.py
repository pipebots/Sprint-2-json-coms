#                                    __
#__________.__             ___.     |__|  __
#\______   \__|_____   ____\_ |__   _||__/  |_  ______
# |     ___/  \____ \_/ __ \| __ \ /  _ \   __\/  ___/
# |    |   |  |  |_> >  ___/| \_\ (  O_O )  |  \___ \
# |____|   |__|   __/ \___  >___  /\____/|__| /____  >
#             |__|        \/    \/                 \/
# Python module to run on pi to listen for JSON doc and parse contents, also sends JSON via serial to ardunio

import serial
import json
import time

#Connect serial and start timer
ser = serial.Serial('/dev/ttyACM0', 115200) #address when using USB cable to arduino
ser.flushInput()
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = timestr + "-sprintbot-data.txt"
start = time.time()

# function to read JSON doc from serial and add a timestamp
def listenJSON():
    try:
        readStr = ser.readline() #doc is sent with line end termination
        readJson = json.loads(readStr)
        timestamp = {"elapsedTime":"{:0.3f}".format(time.time()-start)}
        readJson.update(timestamp) #append timestamp to JSON file
        return readJson

    except:
        #print(readStr)
        print("not valid json") #At the start it is common for a partial JSON doc to be recieved and throw an error - this ignores it
        pass

# function to save json doc
def saveJSON(readJson):
    with open(filename, 'a') as outfile:
        json.dump(readJson, outfile,indent=4) #save to file
            
#function to send data formatted as JSON doc over serial
def writeJSON(doc):
    sendStr = json.dumps(doc, separators=(',',':')) + "\n"
    ser.write(sendStr.encode('utf-8')) #has to be encoded into bits for .write
