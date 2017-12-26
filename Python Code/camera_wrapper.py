import serial
import time
import numpy as np

class CameraWrapper:
	
	# Initializes a connection to a camera on COM port com_port
	# initialize with an empty string to start in dummy mode, with
	# no connection to camera
	def __init__(self, com_port):
		self.dummy_mode = False
		
		if(com_port == ""):
			#start a dummy camera for offline testing
			self.dummy_mode = True
			self.ser = None
			return
	
		self.ser = serial.Serial(com_port,38400,timeout = 3)
		line = ser.readline()
		while(line != "Ready\r\n"):
			line = ser.readline()
		time.sleep(0.5)
			
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		# Cleanup by closing serial port
		if(self.dummy_mode == False):
			self.ser.close()

	# Instructs the camera gimbal to move to angle in the format 
	# [yaw, pitch], then returns the [r, g, b] color value detected
	def get_pixel(self, angle):
		if(self.dummy_mode):
			return np.array([1,2,3])
		
		command_string = "" + angle[0] + " " + angle[1] + " \r\n"
		ser.write(command_string)
		line = ser.readline()
		rgb =  np.fromstring(line, dtype=int, sep=' ')[0:3]
		return rgb