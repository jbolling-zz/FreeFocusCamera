#include <SoftwareSerial.h>
#include "DynamixelMotor.h"

// id of the motor
DynamixelID pitch_id=2;
DynamixelID yaw_id=1;
// speed, between 0 and 1023
int16_t speed=512;

// communication baudrates
const long unsigned int motor_baudrate = 1000000;
const long unsigned int serial_baudrate = 38400;

// hardware serial without tristate buffer
// see blink_led example, and adapt to your configuration
#define SOFT_RX_PIN 6
#define SOFT_TX_PIN 5

SoftwareDynamixelInterface interface(SOFT_RX_PIN, SOFT_TX_PIN);
DynamixelMotor pitch_motor(interface, pitch_id);
DynamixelMotor yaw_motor(interface, yaw_id);

//DynamixelDevice broadcast_device(interface, BROADCAST_ID);

String inString = "";
uint16_t yaw_position;
uint16_t pitch_position;

enum readerState {y_pos, p_pos, finish};

void output_status(uint8_t yaw_s, uint8_t pitch_s, String note){
  Serial.println("[yaw, pitch] " + note + " status:");
  Serial.println((String)"[" + yaw_s + ", " + pitch_s + "]");
}

void output_status(uint16_t yaw_s, uint16_t pitch_s, String note){
  Serial.println("[yaw, pitch] " + note + " status:");
  Serial.println((String)"[" + yaw_s + ", " + pitch_s + "]");
}

void goto_positions(uint16_t yaw, uint16_t pitch){
  yaw_motor.goalPosition(yaw);
  delay(500);
  pitch_motor.goalPosition(pitch);
  delay(500);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(serial_baudrate);
  interface.begin(motor_baudrate);
  delay(100);
  
  // Initialize Motors
  uint8_t yaw_status = yaw_motor.init();
  uint8_t pitch_status=pitch_motor.init();
  delay(100);
  output_status(yaw_status,pitch_status, "init");
  
  yaw_motor.enableTorque();
  pitch_motor.enableTorque();
  delay(100);

  yaw_motor.jointMode(300,724);
  pitch_motor.jointMode(300,724);
  delay(100);
  
  yaw_motor.speed(speed);
  pitch_motor.speed(speed);
  delay(100);
  
  yaw_position = 512;
  pitch_position = 512;

  //initialize TCS Color Sensor
  
}

void loop() {
  // Read serial input:
  readerState state = y_pos;
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    switch (state){
      case y_pos:
        if (isDigit(inChar)) {
          inString += (char)inChar;
        }
        else {
          yaw_position = inString.toInt();
          inString = "";
          state = p_pos;
        }
        break;
      case p_pos:
        if (isDigit(inChar)) {
          inString += (char)inChar;
        }
        else {
          pitch_position = inString.toInt();
          inString = "";
          state = finish;
        }
        break;
      case finish:
        break;
    }
  }
  goto_positions(yaw_position, pitch_position);
  //output_status(yaw_position, pitch_position, "position");
}

