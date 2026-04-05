#include <Servo.h>

Servo servos[5];

int pins[5] = {9, 10, 5, 6, 3};  // Thumb → Pinky

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 5; i++) {
    servos[i].attach(pins[i]);
  }
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');

    for (int i = 0; i < 5; i++) {
      if (data[i] == '1') {
        servos[i].write(90);   // finger ON
      } else {
        servos[i].write(0);    // finger OFF
      }
    }
  }
}