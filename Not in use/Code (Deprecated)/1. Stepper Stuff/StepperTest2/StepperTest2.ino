

#include "MultiStepper.h"
#include "AccelStepper.h"
#include "math.h"

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
//You can still use all the other types of motors supported by accelstepper library (e.g. 4 for a 
//normal 4 wire step motor, 8 for a halfstepped normal 4 wire motor etc.) 
AccelStepper stepperB(4, in1Pin2, in2Pin2, in3Pin2, in4Pin2);

float speeds = 300.0;


void moveToXY(int x, int y)
{
  int dA = x + y - stepperA.currentPosition();
  int dB = x - y - stepperB.currentPosition();
  if (stepperA.distanceToGo() == 0)
  {
    stepperA.move(dA);
   }

  if (stepperB.distanceToGo() == 0)
  {
    stepperB.move(dB);
  }

dA = 0;
dB = 0;


//delay(1000);
//while ((stepperA.currentPosition() != x+y) && (stepperB.currentPosition() != x-y))
//{
  stepperA.run();
  stepperB.run();
//}
//return true;
}


void setup()
{  


  
  
  stepperA.setMaxSpeed(speeds); //max speed of the first motor - modify if you want to
  stepperA.setAcceleration(1000); // rate at which the first motor accelerate -
//  stepperA.moveTo(10);
//  stepperA.run();

  stepperB.setMaxSpeed(speeds);
  stepperB.setAcceleration(1000);
//  stepperB.moveTo(10);
//  stepperB.run();
//
//stepperA.moveTo(10);
//  stepperA.run();
//
//stepperB.moveTo(10);
//  stepperB.run();


  Serial.begin(9600);



  


}


int t = 0;
bool inPos = true;

void loop()
{    
t = t + 1;

//if ((t % 4 == 1) && (inPos == true))
//{
//  inPos = moveToXY(500,0);
//  Serial.println(t); 
//}
//
//if ((t % 4 == 2) && (inPos == true))
//{
////  inPos = moveToXY(500,500);
//  Serial.println(t); 
//}
//
//if ((t % 4 == 3) && (inPos == true))
//{
////  inPos = moveToXY(0,500);
//  Serial.println(t); 
//}
//
//if ((t % 4 == 0) && (inPos == true))
//{
////  inPos = moveToXY(0,0);
//  Serial.println(t); 
//}


moveToXY(0,0);
//Serial.println(t); 
//moveToXY(0,500);
moveToXY(2000,0);
//moveToXY(500,0);
//moveToXY(0,0);
//
//if (inPos == true) {
//  inPos = moveToXY(500,0);
//}
//
//if (inPos == true) {
//  inPos = moveToXY(0,500);
//}
//
//if (inPos == true) {
//  inPos = moveToXY(-500,0);
//}
//
//if (inPos == true) {
//  inPos = moveToXY(0,-500);
//}



//  t = t + 1;
//  if (t == 360)
//  {
//    t = 0;
//  }
//  Serial.println(t); 
//  moveToXY(500*cos(t*PI/180),500*sin(t*PI/180));

//Serial.print(t); 

//moveToXY(0,0);

//moveToXY(0,0);


//stepperB.moveTo(-500);
//stepperB.run();
//stepperB.moveTo(500);
//stepperB.run();






    


}
