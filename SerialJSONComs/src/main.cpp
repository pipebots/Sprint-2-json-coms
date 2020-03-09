/* Arduino code to send data using JSON formal via serial */

#include <Arduino.h>
#include <ArduinoJson.h>
#include <Arduino_LSM9DS1.h> //IMU
#include <MadgwickAHRS.h> //for filtering & fusing IMU data
#include <rgbLED.cpp>

//function declarations-----------
void readIMU();
void sendData();
int listenJSON();
//end funct decs --------------

Madgwick filter;

long currentMillis1, prevMillis1 = 0;
int time1 = 50; //IMU read delay
float ax, ay, az, gx, gy, gz, roll, pitch, yaw = 0;
int range = 0;

void setup() {
    Serial.begin(9600);
    Serial.println("Started");

  //setup IMU --------------------------------------------------
    if (!IMU.begin()) {
      Serial.println("Failed to initialize IMU!");
    }
    filter.begin(1000/time1); //sample rate in Hz
    // Accelerometer range is set at [-4,+4]g -/+0.122 mg
    // Gyroscope range is set at [-2000, +2000] dps +/-70 mdps
   // both 104Hz sample rate}
}

void loop() {

  readIMU();
  sendData();
  redLED();
//  listenJSON();

}

void readIMU(){
    currentMillis1 = millis();
  if (currentMillis1 - prevMillis1 >= time1) {
       prevMillis1 = currentMillis1;
       if (IMU.accelerationAvailable()) { //are these ifs required?
        IMU.readAcceleration(ax, ay, az); //output in g
      }
       if (IMU.gyroscopeAvailable()) {
       IMU.readGyroscope(gx, gy, gz); //output in degrees per second
      }
      filter.updateIMU(gx, gy, gz, ax,ay, az);
      roll = filter.getRoll();
      pitch = filter.getPitch();
      yaw = filter.getYaw();
  }
}

void sendData(){
/*JSON Doc format
{
  "range":999.99,
  "imu": [
    999.99,
    999.99,
    999.99
  ]
}
*/
const size_t capacity = JSON_ARRAY_SIZE(3) + JSON_OBJECT_SIZE(4);
StaticJsonDocument<capacity> doc;

doc["range"] = range;

JsonArray imu = doc.createNestedArray("imu");
imu.add(roll);
imu.add(pitch);
imu.add(yaw);

serializeJson(doc, Serial);
Serial.println("");

}

int listenJSON(){
  if(Serial.available()){
    StaticJsonDocument<100> readJson;
    deserializeJson(readJson,Serial1);
    int led = readJson["LED"];
    return led;
  }
}
