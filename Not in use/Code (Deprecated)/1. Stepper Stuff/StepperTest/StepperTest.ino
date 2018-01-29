/*
  Adafruit Arduino - Lesson 16. Stepper
*/

#include <Stepper.h>

int in1Pin1 = 12;
int in2Pin1 = 11;
int in3Pin1 = 10;
int in4Pin1 = 9;

int in1Pin2 = 6;
int in2Pin2 = 5;
int in3Pin2 = 4;
int in4Pin2 = 3;
int timeout = 1000;

Stepper motor1(200, in1Pin1, in2Pin1, in3Pin1, in4Pin1);
Stepper motor2(200, in1Pin2, in2Pin2, in3Pin2, in4Pin2);

void setup()
{
  pinMode(in1Pin1, OUTPUT);
  pinMode(in2Pin1, OUTPUT);
  pinMode(in3Pin1, OUTPUT);
  pinMode(in4Pin1, OUTPUT);

  pinMode(in1Pin2, OUTPUT);
  pinMode(in2Pin2, OUTPUT);
  pinMode(in3Pin2, OUTPUT);
  pinMode(in4Pin2, OUTPUT);

  // this line is for Leonardo's, it delays the serial interface
  // until the terminal window is opened
//  while (!Serial);

  Serial.begin(9600);
  motor1.setSpeed(150);
  motor2.setSpeed(150);
}

//Check for inactivity and turn off the steppers coils to save battery.
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

void move_motor1(int x) {
  motor1.step(x);
  CheckTimeout(1);
}

void move_motor2(int x) {
  motor2.step(x);
  CheckTimeout(2);
}



void loop()
{
  if (Serial.available())
  {
    int steps = Serial.parseInt();

////    if (steps < 0){
////      for (int i = 0; i < abs(steps); i++){
////      
////        motor1.step(-5);
////        CheckTimeout(1);
////        motor2.step(-5);
////        CheckTimeout(2);
////      }
////    } else{
////      for (int i = 0; i < abs(steps); i++){
////      
////        motor1.step(5);
////        CheckTimeout(1);
////        motor2.step(5);
////        CheckTimeout(2);
////      }
////    }


//    motor1.step(steps);
  move_motor1(steps);
//    CheckTimeout(1);
//    delay(1000);
//    motor2.step(steps);
  move_motor2(steps);
//    CheckTimeout(2);
    

    
  }
}
