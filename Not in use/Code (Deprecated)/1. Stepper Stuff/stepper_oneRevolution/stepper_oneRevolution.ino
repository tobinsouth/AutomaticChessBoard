/*     Simple Stepper Motor Control Exaple Code
 *      
 *  by Dejan Nedelkovski, www.HowToMechatronics.com
 *  
 */
 
// defines pins numbers
const int stepPinA = 3; 
const int dirPinA = 4; 
const int stepPinB = 6; 
const int dirPinB = 7; 
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPinA,OUTPUT); 
  pinMode(dirPinA,OUTPUT);
  pinMode(stepPinB,OUTPUT); 
  pinMode(dirPinB,OUTPUT);


  Serial.begin(9600);
}

int currentX = 0;
int currentY = 0;

int pulse = 50;


int moveX(int x, int stepDel = 50) {
//  int dX = x - currentX;
  if (x > 0) {
    digitalWrite(dirPinA,HIGH);
    digitalWrite(dirPinB,HIGH);
    for (int i = 0; i < x*100; i++) {
      digitalWrite(stepPinA,HIGH);
      digitalWrite(stepPinB,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinA,LOW);
      digitalWrite(stepPinB,LOW); 
      delayMicroseconds(stepDel);
    }
  } else {
    digitalWrite(dirPinA,LOW);
    digitalWrite(dirPinB,LOW);
    for (int i = 0; i < -x*100; i++) {
      digitalWrite(stepPinA,HIGH);
      digitalWrite(stepPinB,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinA,LOW);
      digitalWrite(stepPinB,LOW); 
      delayMicroseconds(stepDel);
    }
  }
}

void moveY(int y, int stepDel = 50) {
//  int dY = y - currentY;
  if (y > 0) {
    digitalWrite(dirPinA,HIGH);
    digitalWrite(dirPinB,LOW);
    for (int i = 0; i < y*100; i++) {
      digitalWrite(stepPinA,HIGH);
      digitalWrite(stepPinB,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinA,LOW);
      digitalWrite(stepPinB,LOW); 
      delayMicroseconds(stepDel);
    }
  } else {
    digitalWrite(dirPinA,LOW);
    digitalWrite(dirPinB,HIGH);
    for (int i = 0; i < -y*100; i++) {
      digitalWrite(stepPinA,HIGH);
      digitalWrite(stepPinB,HIGH); 
      delayMicroseconds(pulse); 
      digitalWrite(stepPinA,LOW);
      digitalWrite(stepPinB,LOW); 
      delayMicroseconds(pulse);
    }
  }
//  currentY = currentY + y;

}


void moveA(int a, int stepDel = 50) {
  if (a > 0) {
    digitalWrite(dirPinA,HIGH); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for(int i = 0; i < a*100; i++) {
      digitalWrite(stepPinA,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinA,LOW); 
      delayMicroseconds(stepDel); 
    }
  } else {
    digitalWrite(dirPinA,LOW); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for(int i = 0; i < -a*100; i++) {
      digitalWrite(stepPinA,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinA,LOW); 
      delayMicroseconds(stepDel); 
    }
  }
}

void moveB(int b, int stepDel = 50) {
  if (b > 0) {
    digitalWrite(dirPinB,HIGH); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for(int i = 0; i < b*100; i++) {
      digitalWrite(stepPinB,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinB,LOW); 
      delayMicroseconds(stepDel); 
    }
  } else {
    digitalWrite(dirPinB,LOW); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for(int i = 0; i < -b*100; i++) {
      digitalWrite(stepPinB,HIGH); 
      delayMicroseconds(stepDel); 
      digitalWrite(stepPinB,LOW); 
      delayMicroseconds(stepDel); 
    }
  }
}

int xMove;
int yMove;
int aMove;
int bMove;
bool mag;
String incomingByte;

void loop() {

  xMove = 0;
  yMove = 0;
  aMove = 0;
  bMove = 0;
  mag = 0;
//  str 
//
//  while (Serial.available() <= 0) {
//    xMove = Serial.read();
//    while (Serial.available() <= 0) {
//      yMove = Serial.read();
//      while (Serial.available() <= 0) {
//        aMove = Serial.read();
//        while (Serial.available() <= 0) {
//          bMove = Serial.read();
//          while (Serial.available() <= 0) {
//            mag = Serial.read();
//
//            moveX(xMove);
//            delay(100);
//  moveY(yMove);
//  delay(100);
//  moveA(aMove);
//  delay(100);
//  moveB(bMove);
//  delay(100);
//            
//          }
//        }
//      }
//    }
//  }


if (Serial.available() > 0) {

incomingByte = Serial.readString(); // read the incoming byte:

Serial.print(" I received:");

Serial.println(incomingByte);

}

//  moveX(10);

//moveX(290);
//delay(100);
//moveY(325);
//delayMicroseconds(1);
//moveY(30);
//delay(100);
//moveX(-290);
//delay(100);
//moveY(-325);
//delayMicroseconds(1);
//moveY(-30);
//delay(100);
//
//moveA(300);
//delay(100);


//moveB(100);
//delay(100);
//moveB(-100);
//delay(100);
//moveA(100);
//delay(100);
//moveB(100);
//delay(100);
//moveA(-100);
//delay(100);
//moveB(-100);
//delay(100);

//moveX(100);
//delay(100);
//moveX(-100);
//delay(100);
//moveY(100);
//delay(100);
//moveY(-100);
//delay(100);














}


