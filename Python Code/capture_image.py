import sys
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from image_templates import *
from camera_wrapper import *
#from scipy.misc import imsave
import cv2 as cv

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
with CameraWrapper('COM3') as wrapper:
	# Read pixels one by one from camera
	for i in range(0,M):
		for j in range(0,N):
			pixels[i,j,:] = wrapper.get_pixel(angles[i,j,:])
			print 'Pixel returned from camera:'
			print("(" + str(i) + "," + str(j) + "): " + str(pixels[i,j,:]))
			
# Show image
imgplot = plt.imshow(pixels)
cv.imwrite('output.png',pixels)
np.save('output.npz',pixels)

plt.show(block=True)