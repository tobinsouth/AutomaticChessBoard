#include "MultiStepper.h"
#include "AccelStepper.h"

int in1Pin1 = 12;
int in2Pin1 = 11;
int in3Pin1 = 10;
int in4Pin1 = 9;

int in1Pin2 = 6;
int in2Pin2 = 5;
int in3Pin2 = 4;
int in4Pin2 = 3;

int buttonX = 7;
int buttonY = 2;

// Define some steppers and the pins the will use
AccelStepper stepperA(4, in1Pin1, in2Pin1, in3Pin1, in4Pin1);
//You can still use all the other types of motors supported by accelstepper library (e.g. 4 for a normal 4 wire step motor, 8 for a halfstepped normal 4 wire motor etc.) 
AccelStepper stepperB(4, in1Pin2, in2Pin2, in3Pin2, in4Pin2);

float speeds = 400.0;
float stepperCirc = 37.7;

int buttonXval = 0;
int buttonYval = 0;

void CheckTimeout(int x){

    if (x == 1){
      digitalWrite(in1Pin1, LOW);
      digitalWrite(in2Pin1, LOW);
      digitalWrite(in3Pin1, LOW);
      digitalWrite(in4Pin1, LOW);
    }
    
    if (x == 2){
      digitalWrite(in1Pin2, LOW);
      digitalWrite(in2Pin2, LOW);
      digitalWrite(in3Pin2, LOW);
      digitalWrite(in4Pin2, LOW);
    }

}


void moveX(int steps)
{
  int x = steps/2;
  stepperA.move(x);
  stepperA.runSpeed();
  stepperB.move(x);
  stepperB.runSpeed();
}

void moveY(int steps)
{
  int x = steps/2;
  int y = -steps/2;
  stepperA.move(x);
  stepperA.runSpeed();
  stepperB.move(y);
  stepperB.runSpeed();
}

void moveToX(int steps)
{
  int x = steps/2;
  stepperA.moveTo(x);
  stepperA.runSpeed();
  stepperA.setSpeed(400);
  stepperB.moveTo(x);
  stepperB.runSpeed();
}

void moveToY(int steps)
{
  int x = steps/2;
  int y = -steps/2;
  stepperA.moveTo(x);
  stepperA.setSpeed(400);
  stepperA.runSpeed();
  stepperB.moveTo(y);
  stepperB.runSpeed();
}

void moveToXY(long x, long y)
{
  CheckTimeout(1);
   CheckTimeout(2);
   long dA = x + y - stepperA.currentPosition();
   long dB = x - y - stepperB.currentPosition();
   stepperA.move(dA);
   stepperA.run();
//   delay(1000);
   stepperB.move(dB);
   stepperB.runToPosition();
   CheckTimeout(1);
   CheckTimeout(2);
}

void setup()
{
  stepperA.setMaxSpeed(speeds); //max speed of the first motor - modify if you want to
  stepperA.setAcceleration(20000.0); // rate at which the first motor accelerate -

  stepperB.setMaxSpeed(speeds);
  stepperB.setAcceleration(20000.0);
  
  stepperA.setSpeed(400);
  
  Serial.begin(9600);

  pinMode(buttonX, INPUT);
  pinMode(buttonY, INPUT);

  int buttonXval = 0;
  int buttonYval = 0;

//  while (buttonXval == LOW) 
//  {
//    buttonXval = digitalRead(buttonX);
//    moveX(1000);
////    stepperA.move(100);
////    stepperA.setSpeed(400);
////    stepperA.runSpeed();
//    
//  }

//  delay(1000);
  
//  while (buttonYval == LOW) 
//  {
//    buttonYval = digitalRead(buttonY);
//    moveY(1000);
//  }

  stepperA.setCurrentPosition(0.0);
  stepperB.setCurrentPosition(0.0);

  delay(1000);





}



void loop()
{    
//  CheckTimeout(1);
//  CheckTimeout(2);
//  delay(100);
//  moveToX(400);


  stepperA.runToNewPosition(2000);
  stepperA.runToNewPosition(-2000);
//  stepperA.run();
//  stepperB.runToNewPosition(-1000);
//  stepperA.runToNewPosition(-1000);
//  stepperA.run();


//  moveToXY(200,200);
//  moveToXY(-100,-100);
//  moveToXY(0,0);
//  
//  stepperB.moveTo(1000);
//  stepperA.moveTo(-1000);
//  stepperA.run();
//  stepperB.run();


  
}
