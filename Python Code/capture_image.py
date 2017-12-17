import serial
import time
import numpy as np

ser = serial.Serial('COM3',38400,timeout = 3)

line = ser.readline()
while(line != "Ready\r\n"):
	line = ser.readline()
time.sleep(0.5)

print "requesting pixel"
ser.write(b'512 512 \r\n')
line = ser.readline()
line.split(" ")
print line
ser.close()