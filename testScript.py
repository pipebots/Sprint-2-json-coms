#testing pi_com.py module for use via T4
import pi_coms as com
import time

i=0
while True:
    com.listenJSON()
    x = {
        'LED':i,
        'mv_case':0
        'spd_limit':0
        }
         
    com.writeJSON(x)
    
    i=i+1
    if i == 8:
        i=0
    time.sleep(0.25) #so it can be seen when debugging