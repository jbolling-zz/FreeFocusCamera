import serial
import time
import sys
import numpy as np
from image_templates import *

#Get template files and sanitize
if(len(sys.argv) == 1):
	print('Syntax - capture_imge.py <template directory>')
	quit()

angles = load_angles(sys.argv[1])
print angles[0,0,:]
print(angles)
	
	
#ser = serial.Serial('COM3',38400,timeout = 3)

#line = ser.readline()
#while(line != "Ready\r\n"):
#	line = ser.readline()
#time.sleep(0.5)

print "requesting pixel"
#ser.write(b'512 512 \r\n')
#line = ser.readline()
line = "1 2 3 \b\n"
vals =  np.fromstring(line, dtype=int, sep=' ')[0:3]

#ser.close()