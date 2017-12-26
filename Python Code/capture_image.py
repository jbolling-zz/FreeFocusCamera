import sys
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from image_templates import *
from camera_wrapper import *

# Read in angle data from template file
if(len(sys.argv) == 1):
	print('Syntax - capture_imge.py <template directory>')
	quit()
angles = load_angles(sys.argv[1])

# Construct pixel array
M = angles.shape[0]
N = angles.shape[1]
pixels = np.zeros((M,N,3))

# Open camera connection
print "Connecting to camera"
with CameraWrapper("") as wrapper:
	# Read pixels one by one from camera
	for i in range(0,M):
		for j in range(0,N):
			pixels[i,j,:] = wrapper.get_pixel(angles[i,j,:])
			print 'Pixel returned from camera'
			
# Show image
imgplot = plt.imshow(pixels)
plt.show(block=True)