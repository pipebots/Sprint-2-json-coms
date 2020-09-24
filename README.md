# Sprint-2-json-coms
## Code to send data between Arduino Nano 33 BLE Sense and a Raspberry Pi using serial via USB cable.

Test setup 
- sends imu data from arduino to pi 
- sends numbers from pi to arduino which change the colour of the onboard RGB LED. 

### Contents
- SerialJSONComs - This folder is a platformio project containing the ardunio code for a nano ble sense. (src>main.cpp is the main file!)
- pi_com.py should be imported into other scripts for use.
- testScript.py shows this in practice. 
- pi_coms_test.py is a standalone script, file mainly kept as a record with some useful comments as examples of how to extract items from the JSON doc.

