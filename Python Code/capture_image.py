import sys
import numpy as np
from image_templates import *
from camera_wrapper import *

#Get template files and sanitize
if(len(sys.argv) == 1):
	print('Syntax - capture_imge.py <template directory>')
	quit()

angles = load_angles(sys.argv[1])
print angles[0,0,:]
M = angles.shape[0]
N = angles.shape[1]
pixels = np.zeros((M,N,3))

print "Connecting to camera"
with CameraWrapper("") as wrapper:
	print "Requesting Pixel"
	print wrapper.get_pixel([0,0])