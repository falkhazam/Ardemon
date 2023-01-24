// ----------------------------------------------------------------------------------------------------
// =========== Accelerometer Sensor ============ 
// ----------------------------------------------------------------------------------------------------

/*
 * Configure the analog input pins to the accelerometer's 3 axes
 */
const int X_PIN = A2;
const int Y_PIN = A3;
const int Z_PIN = A4;

/*
 * Set the "zero" states when each axis is neutral
 * NOTE: Customize this for your accelerometer sensor!
 */
const int X_ZERO = 1985;
const int Y_ZERO = 1985;
const int Z_ZERO = 2425;


/*
 * Configure the analog pins to be treated as inputs by the MCU
 */
void setupAccelSensor() {
  pinMode(X_PIN, INPUT);
  pinMode(Y_PIN, INPUT);
  pinMode(Z_PIN, INPUT);
}

/*
 * Read a sample from the accelerometer's 3 axes
 */
void readAccelSensor() {
  ax = analogRead(X_PIN); 
  ay = analogRead(Y_PIN);
  az = analogRead(Z_PIN);
}

/*
 * Get the orientation of the accelerometer
 * Returns orientation as an integer:
 * 0 == flat
 * 1 == left and shoot
 * 2 == right and shoot
 * 3 == left
 * 4 == right
 * 5 == shoot
 */
int getOrientation() {
  int orientation = 0;

  // Subtract out the zeros
  int x = ax - X_ZERO;
  int y = ay - Y_ZERO;
  int z = az - Z_ZERO;

  buttonState = digitalRead(buttonPin);

//button LOW is fired, ax is which direction

  //check if upside down, if so dont do anything until it is right side up


  if (lives == -1) {
     String messageEnd = ("GAME OVER!");
     writeDisplay(messageEnd.c_str(), 2, true);
     
  }
  else if (az < 2000) {
     writeColor(200,00,0);
     deactivateMotor();
     activateMotor(255);
     String messageScore = ("SIT UP STRAIGHT");
     writeDisplay(messageScore.c_str(), 1, true);
    
  }
  else {
    deactivateMotor();
    writeColor(0,0,0);
    String messageScore = "Score: " + String(score);
    writeDisplay(messageScore.c_str(), 1, true);
    String messageLives = "Lives: " + String(lives);
    writeDisplay(messageLives.c_str(), 2, true);
  }
  
  
  if (buttonState == LOW && ax > 2075) {
    orientation = 2;
  }
  else if (buttonState == LOW && ax < 1750) {
    orientation = 1;
  }

  else if (ax > 2075) {
    orientation = 4;
    
  }

  else if ( ax < 1750 ) {
    orientation = 3;
  }
  else if (buttonState == LOW) {
    orientation  = 5;
  }
  else {
    orientation = 0;
  }

  
//  else if(abs(x) >= abs(y) && abs(x) >= abs(z)) {
//    if( x < 0 ) // left
//      orientation = 3;
//    else
//      orientation = 4;
//  }
//  // If ay has biggest magnitude, it's either up or down
//  else if(abs(y) >= abs(x) && abs(y) >= abs(z)) {
//    if( y < 0 ) // up
//      orientation = 1;
//    else // down
//      orientation = 2;
//  }
//  // If az biggest magnitude, it's flat (or upside-down)
//  else if(abs(z) > abs(x) && abs(z) >= abs(y)) {
//    orientation = 0; // flat
//  }


  return orientation;
}
