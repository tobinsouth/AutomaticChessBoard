#include <Servo.h>

Servo magnet;

// defines pins numbers
const int stepPinA = 3; // Yellow
const int dirPinA = 4;  // Green
const int stepPinB = 6;
const int dirPinB = 7;
const int squareMult = 1625; // *2
const int diagMult = 2;


int magLow = 120;
int magHigh = 170;
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


int n;
int stepSpeed = 50;
int magTog = 0;
int incomingList[150];
int bytesToRead;




void loop() {



  n = 0;
  bytesToRead = Serial.available();
  while (Serial.available() > 4) {
    delay(50);
//    Serial.print("Serial.available() is: ");
//    Serial.println(Serial.available());
//    bytesToRead = Serial.available();
//    Serial.print("bytesToRead is: ");
//    Serial.println(bytesToRead);
    for (int i = 0; i < 5; i++) {
      incomingList[n] = Serial.read() - 70;
      n++;
    }
  }
//  Serial.print("The n is: ");
//  Serial.println(n);

  for (int i = 0; i < n; i += 5) {
//    Serial.print("The index is: ");
//    Serial.println(i);
//    for (int j = 0; j < 5; j++) {
//      Serial.println(incomingList[i + j]);
//    }

    moveX(incomingList[i], stepSpeed);

    moveY(incomingList[i + 1], stepSpeed);

    moveA(incomingList[i + 2], stepSpeed);

    moveB(incomingList[i + 3], stepSpeed);

    magTog = incomingList[i + 4] / 2;

    moveMag(magTog);

    if (magTog == 1) {
      stepSpeed = 75;
    }
    else {
      stepSpeed = 45;
    }
    delay(500);
  }
  while (Serial.available() < 1) {
    Serial.print("x");
  }


}










