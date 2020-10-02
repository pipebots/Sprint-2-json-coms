#testing pi_com.py module for use via T4
import pi_coms as com
import time

i=0
x = {
    'auto_case':0,
    'spd_limit':0.6,
    'timeout':1000
    }

while True:
    doc = com.listenJSON() 
    print(doc)
    #data can be parsed from the doc here e.g:
    #wheel1Pos = doc["wheel1Pos"]
    
    #only needed if you want to keep the data
    com.saveJSON(doc) 

    # Send doc to arduino, can be partially filled.
    com.writeJSON(x)
    
    # set to same speed arduino is outputting, helps it to not read partial docs.
    # obviously dont use this blocking function in a proper program.
    time.sleep(0.05) 
