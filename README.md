# Sprint-2-json-coms
## Code to send data between Arduino Nano 33 BLE Sense and a Raspberry Pi using serial via USB cable.
Test setup 
- sends imu data from arduino to pi 
- sends numbers from pi to arduino which change the colour of the onboard RGB LED. 

### Contents
- SerialJSONComs - This folder is a platformio project containing the ardunio code for a nano ble sense. (src>main.cpp is the main file!)
- pi_coms_2.py - code to run on pi to listen and send via serial

