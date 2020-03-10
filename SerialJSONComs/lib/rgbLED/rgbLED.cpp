// RGB LED Functions
#include <Arduino.h>

//pins for build in led on nano 33 sense
#define R_LED_PIN         22
#define G_LED_PIN         23
#define B_LED_PIN         24

void greenLED(){
    analogWrite(R_LED_PIN,UINT8_MAX);
    analogWrite(G_LED_PIN,0);
    analogWrite(B_LED_PIN,UINT8_MAX);
}
void blueLED(){
    analogWrite(R_LED_PIN,UINT8_MAX);
    analogWrite(G_LED_PIN,UINT8_MAX);
    analogWrite(B_LED_PIN,0);
}
void redLED(){
    analogWrite(R_LED_PIN,0);
    analogWrite(G_LED_PIN,UINT8_MAX);
    analogWrite(B_LED_PIN,UINT8_MAX);
}
void yellowLED(){
    analogWrite(R_LED_PIN,0);
    analogWrite(G_LED_PIN,0);
    analogWrite(B_LED_PIN,UINT8_MAX);
}
void magentaLED(){
    analogWrite(R_LED_PIN,0);
    analogWrite(G_LED_PIN,UINT8_MAX);
    analogWrite(B_LED_PIN,0);
}
void cyanLED(){
    analogWrite(R_LED_PIN,UINT8_MAX);
    analogWrite(G_LED_PIN,0);
    analogWrite(B_LED_PIN,0);
}
void offLED(){
    analogWrite(R_LED_PIN,UINT8_MAX);
    analogWrite(G_LED_PIN,UINT8_MAX);
    analogWrite(B_LED_PIN,UINT8_MAX);
}
void whiteLED(){
    analogWrite(R_LED_PIN,0);
    analogWrite(G_LED_PIN,0);
    analogWrite(B_LED_PIN,0);
}
void rgbLED(int r,int g,int b){
    analogWrite(R_LED_PIN,r);
    analogWrite(G_LED_PIN,g);
    analogWrite(B_LED_PIN,b);
}
