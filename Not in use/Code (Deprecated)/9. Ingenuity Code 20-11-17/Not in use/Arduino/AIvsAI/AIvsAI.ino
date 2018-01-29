#include <Servo.h>

Servo magnet;

// defines pins numbers
const int stepPinA = 3; // Yellow
const int dirPinA = 4;  // Green
const int stepPinB = 6;
const int dirPinB = 7;
const int squareMult = 1625; // *2
const int diagMult = 2;


int magLow = 85;
int magHigh = 150;
//2055;
//1265

//#define INPUT_SIZE 14;

void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPinA, OUTPUT);
  pinMode(dirPinA, OUTPUT);
  pinMode(stepPinB, OUTPUT);
  pinMode(dirPinB, OUTPUT);

  Serial.begin(9600);

  magnet.attach(9);
  magnet.write(magLow);


}


// 11 squares = 44.7cm (in x +ve) like 0.1cm from (0,0)
// 9 squares = 36.6cm (in y +ve) 1.3cm away from (0,0)




void moveMag(int tog) {
  if (tog == 0) {
    magnet.write(magLow);
  }
  else {
    magnet.write(magHigh);
  }
}

void moveY(int hDist, int stepDel = 50) {
  if (hDist > 0) {
    digitalWrite(dirPinA, LOW);
    digitalWrite(dirPinB, LOW);
    for (int i = 0; i < hDist * squareMult; i++) {
      digitalWrite(stepPinA, HIGH);
      digitalWrite(stepPinB, HIGH);
      delayMicroseconds(stepDel);
      digitalWrite(stepPinA, LOW);
      digitalWrite(stepPinB, LOW);
      delayMicroseconds(stepDel);
    }
  } else {
    digitalWrite(dirPinA, HIGH);
    digitalWrite(dirPinB, HIGH);
    for (int i = 0; i < -hDist * squareMult; i++) {
      digitalWrite(stepPinA, HIGH);
      digitalWrite(stepPinB, HIGH);
      delayMicroseconds(stepDel);
      digitalWrite(stepPinA, LOW);
      digitalWrite(stepPinB, LOW);
      delayMicroseconds(stepDel);
    }
  }
}

void moveX(int hDist, int stepDel = 50) {
  if (hDist > 0) {
    digitalWrite(dirPinA, HIGH);
    digitalWrite(dirPinB, LOW);
    for (int i = 0; i < hDist * squareMult; i++) {
      digitalWrite(stepPinA, HIGH);
      digitalWrite(stepPinB, HIGH);
      delayMicroseconds(stepDel);
      digitalWrite(stepPinA, LOW);
      digitalWrite(stepPinB, LOW);
      delayMicroseconds(stepDel);
    }
  } else {
    digitalWrite(dirPinA, LOW);
    digitalWrite(dirPinB, HIGH);
    for (int i = 0; i < -hDist * squareMult; i++) {
      digitalWrite(stepPinA, HIGH);
      digitalWrite(stepPinB, HIGH);
      delayMicroseconds(stepDel);
      digitalWrite(stepPinA, LOW);
      digitalWrite(stepPinB, LOW);
      delayMicroseconds(stepDel);
    }
  }
}

void moveB(int hDist, int stepDel = 50) {
  if (hDist > 0) {
    digitalWrite(dirPinA, LOW); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for (int j = 0; j < 2; j++) {
      for (int i = 0; i < hDist * squareMult; i++) {
        digitalWrite(stepPinA, HIGH);
        delayMicroseconds(stepDel * 0.75);
        digitalWrite(stepPinA, LOW);
        delayMicroseconds(stepDel * 0.75);
      }
    }
  } else {
    digitalWrite(dirPinA, HIGH); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for (int j = 0; j < 2; j++) {
      for (int i = 0; i < -hDist * squareMult; i++) {
        digitalWrite(stepPinA, HIGH);
        delayMicroseconds(stepDel * 0.75);
        digitalWrite(stepPinA, LOW);
        delayMicroseconds(stepDel * 0.75);
      }
    }
  }
}

void moveA(int hDist, int stepDel = 50) {
  if (hDist > 0) {
    digitalWrite(dirPinB, LOW); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for (int j = 0; j < 2; j++) {
      for (int i = 0; i < hDist * squareMult; i++) {
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(stepDel * 0.75);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(stepDel * 0.75);
      }
    }
  } else {
    digitalWrite(dirPinB, HIGH); // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
    for (int j = 0; j < 2; j++) {
      for (int i = 0; i < -hDist * squareMult; i++) {
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(stepDel * 0.75);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(stepDel * 0.75);
      }
    }
  }
}


int i;
int stepSpeed = 50;
int magTog = 0;
int incomingList[5];




void loop() {



  i = 0;
  while (i < 5) {
    if (Serial.available() > 0) {
      incomingList[i] = Serial.read() - 70;
      i++;
    }
  }

  moveX(incomingList[0], stepSpeed);

  moveY(incomingList[1], stepSpeed);

  moveA(incomingList[2], stepSpeed);

  moveB(incomingList[3], stepSpeed);

  magTog = incomingList[4] / 2;

  moveMag(magTog);

  if (magTog == 1) {
    stepSpeed = 75;
  }
  else {
    stepSpeed = 45;
  }
  delay(500);

  while (Serial.available() < 1) {
    Serial.print("x");
  }


}










