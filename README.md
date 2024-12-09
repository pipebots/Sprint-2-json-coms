# Sprint-2-json-coms
## Code to send data between Arduino Nano 33 BLE Sense and a Raspberry Pi using serial via USB cable.

Test setup
- sends imu data from arduino to pi
- sends numbers from pi to arduino which change the colour of the onboard RGB LED.

## Contents
- SerialJSONComs - This folder is a platformio project containing the ardunio code for a nano ble sense. (src>main.cpp is the main file!)
- pi_com.py should be imported into other scripts for use.
- testScript.py shows this in practice.
- pi_coms_test.py is a standalone script, file mainly kept as a record with some useful comments as examples of how to extract items from the JSON doc.

# SprintBot API
Low level motor control and sensor polling is done on the Arduino nano sense.
This is connected to the raspberry pi via a usb cable and serial communication is used to pass data between the devices.
This is done using JSON libraries for simplicity, with a new line termination.
The code for this is in Sprint-2-JSON-coms repo.

Pi_coms.py can be imported as a library and called to listen and write to serial and save to file.

# listenJSON()
Function to read JSON doc from serial and add a timestamp.
If successful, returns the json doc with timestamp added.
If read unsuccessful, returns null

### saveJSON()
Function to save JSON doc to txt file.
A time and date stamped file is created when the script starts.
This function appends the json doc to the end.

### writeJSON()
Function to send data formatted as JSON doc over serial

#### JSON Doc
The commands that can be sent are
```
doc = {
        "auto_case":Command to move robot, 0-13 as listed below,
        "spd_limit":Speed limit 0-100%, actual speed will vary due to it ramping up and PID control.
        "timeout":timeout in ms before stop command (case 6) is triggered.
                  Optional, if it is not sent then the sent auto_case will remain until overwritten.
        }
```

## Auto_case
To control the robot a case number can be sent, these correspond to the buttons in the smartphone App which is used to manually control the robot.

Case:

0. LEDs Off
1. LEDs On
2. Forward
3. Backwards
4. Left (turn on the spot one motor forward, the other reverse)
5. Right (turn on the spot one motor forward, the other reverse)
6. Stop
7. Forward Left (Wider turn, one motor off, the other forwards)
8. Forward Right (Wider turn, one motor off, the other forwards)
9. Back Left (Wider turn, one motor off, the other backwards)
10. Back Right (Wider turn, one motor off, the other backwards)
11. (not currently in use: autonomous control)
12. Emergency Stop (Disconnects Bluetooth and stops robot, requires hardware reset on robot so use carefully!)
13. (not currently in use: manual control)

## Acknowledgments

This work is supported by the UK's Engineering and Physical Sciences Research
Council (EPSRC) Programme Grant EP/S016813/1

Copyright (c), 2020, 2024, University of Leeds.

The authors, A. Blight & N. Fry have asserted their moral rights.
