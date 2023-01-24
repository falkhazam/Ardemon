/*
 * Global variables
 */
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; int ay = 0; int az = 0;
int ppg = 0;        // PPG from readPhotoSensor() (in Photodetector tab)
int sampleTime = 0; // Time of last sample (in Sampling tab)
bool sending;
int score = 0;
int lives = 3;


// setup button
const int buttonPin = 14;
int buttonState = 0;

bool gotHit = false;
bool redHit = false;
bool greenHit = false;
bool blueHit = false;
bool purpleHit = false;

//setup led
const int ledR = 33;
const int ledG = 27;
const int ledB = 12;


/*
 * Initialize the various components of the wearable
 */

void writeColor(int r, int g, int b) {
  analogWrite(ledR, r);
  analogWrite(ledG, g);
  analogWrite(ledB, b);
}
void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupPhotoSensor();
  sending = false;
  setupMotor();

  writeDisplay("Ready...", 1, true);
  writeDisplay("Set...", 2, false);
  writeDisplay("Play!", 3, false);

  //setup button
  pinMode(buttonPin, INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  writeColor(0,0,0);
}


/*
 * The main processing loop
 */
void loop() {
  // Parse command coming from Python (either "stop" or "start")
  deactivateMotor();
  String command = receiveMessage();
  if(command == "stop") {
    sending = false;
    writeDisplay("Controller: Off", 0, true);
  }
  else if(command == "start") {
    sending = true;
    writeDisplay("Controller: On", 0, true);
  }
  else if(command == "-1") {
    gotHit = true;
  }
  else if(command == "10") {
    greenHit = true;
    score +=10;
  }
  else if(command == "20") {
    blueHit = true;
    score +=20;
  }
  else if( command == "30" ) {
    purpleHit = true;
    score +=30;
  }
  else if(command == "50") {
    redHit = true;
    score +=50;
  }
  else if(command == "100") {
    redHit = true;
    score +=100;
  }
  else if( command == "150" ) {
    redHit = true;
    score +=150;
  }
  else if( command == "300" ) {
    redHit = true;
    score +=300;
  }

//display score

//motor and led
if (gotHit) {
     gotHit = false;
     lives -=1;
     activateMotor(255);
     delay(500);
     deactivateMotor();
}
else if (greenHit) {
     greenHit = false;
     writeColor(0,200,0);
     delay(100);
     writeColor(0,0,0);

}
else if (blueHit) {
     blueHit = false;
     writeColor(0,50,200);
     delay(100);
     writeColor(0,0,0);

}
else if (purpleHit) {
     purpleHit = false;
     writeColor(200,0,200);
     delay(100);
     writeColor(0,0,0);

}
else if (redHit) {
     redHit = false;
     writeColor(200,00,0);
     delay(100);
     writeColor(0,0,0);

}


  

  // Send the orientation of the board
  if(sending && sampleSensors()) {
    sendMessage(String(getOrientation()));
  }
}
