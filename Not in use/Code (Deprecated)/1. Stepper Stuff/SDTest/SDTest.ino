#include <Servo.h> 

Servo mag;

void setup() 
{ 
  mag.attach(9);
  
}

void loop() {
  mag.write(180);
  delay(1000);
  mag.write(100);
  delay(1000);
}
