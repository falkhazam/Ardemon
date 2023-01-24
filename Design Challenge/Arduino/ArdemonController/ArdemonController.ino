#include <stdio.h>
#include "Button.h"
int sampleTime = 0; // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
int ppg = 0; //Photoresistor values (from readPhotoSensor());
bool sending;

int buzz = 0;
bool alreadyStartedBuzz = false;

const int red = 33;
const int green = 27;
const int blue = 12;

Button button2(14); // Connect your button between pin 2 and GND
//Button button(21);

void setup() {  
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupPhotoSensor();
  setupMotor();
  
  sending = false;
  writeDisplay("Sleep", 0, true);
  
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  writeColor(200,200,200);
}

void writeColor(int r, int g, int b) {
  analogWrite(red, r);
  analogWrite(green, g);
  analogWrite(blue, b);
}

void loop() {
  
  String command = receiveMessage();
  const char* c_com = command.c_str();
  if(command == "sleep") {
    sending = false;
    writeDisplay("Sleep", 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay("Wearable", 0, true);
  }
  
  else if (command == "LAVA") {
    writeColor(200, 0, 0);
  } else if (command == "OCEAN") {
    writeColor(0,0,200);
  } else if (command == "TREE") {
    writeColor(0,200,0);
  } else if (command == "LIGHTNING") {
    writeColor(200,200,0);
  }

  else if(command.endsWith("OLED")){
    clearOLED();
    command = command.substring(0,command.length() - 4);
    writeDisplayCSV(command, 3);
  }

  else if(command == "BUZZ") {
    if (!alreadyStartedBuzz) {
       buzz = millis();
       activateMotor(200);
       alreadyStartedBuzz = true;
    }
   
  }

  if (millis() - buzz > 500) {
    deactivateMotor();
    alreadyStartedBuzz = false;
  }

  if (button2.pressed()) {
    sendMessage("SELECTED");
  }
//
//  if (button2.pressed()) {
//    sendMessage("BATTLE");
//  }
  
  if(sending && sampleSensors()) {
    int orientation = getOrientation();
    if (orientation == 1 || orientation == 2) {
      sendMessage("TILT");
    }
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    sendMessage(response);   
    if (ppg < 8500) {
      sendMessage("PET");
    }
    
  }
}
