#include <SoftwareSerial.h>

// Test motor joint mode

#include "DynamixelMotor.h"

// id of the motor
const uint8_t id=2;


// communication baudrate
const long unsigned int baudrate = 1000000;
const long unsigned int serial_baudrate = 1200;

// hardware serial without tristate buffer
// see blink_led example, and adapt to your configuration
#define SOFT_RX_PIN 3
#define SOFT_TX_PIN 4

SoftwareDynamixelInterface interface(SOFT_RX_PIN, SOFT_TX_PIN);
//HardwareDynamixelInterface interface(Serial);
//DynamixelMotor motor(interface, id);
DynamixelDevice broadcast_device(interface, BROADCAST_ID);

uint8_t led_state=true;

void setup()
{ 
  Serial.begin(serial_baudrate);
  interface.begin(baudrate);
  delay(100);
  
  // check if we can communicate with the motor
  // if not, we turn the led on and stop here
  //uint8_t status=broadcast_device.init();
  //if(status!=DYN_STATUS_OK)
  //{
  //  pinMode(LED_BUILTIN, OUTPUT);
  //  digitalWrite(LED_BUILTIN, HIGH);
  //  while(1);
  //}
  delay(1000);

  uint8_t status = broadcast_device.changeId(2);
  Serial.print(status);
  delay(1000);
  Serial.print(broadcast_device.id());
  delay(1000);

  if(status!=DYN_STATUS_OK)
  {
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
    while(1);
  }
}

void loop() 
{
 
  broadcast_device.write(DYN_ADDRESS_LED, led_state);
  led_state=!led_state;
  Serial.print(broadcast_device.status());
  delay(1000);
  
  //motor.led(HIGH);
  //delay(1000);
  //motor.led(LOW);
  //delay(1000);
}
