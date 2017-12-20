import csv
import os.path as path
import os
import numpy as np

#Returns a MxNx2 array of [yaw, pitch] pairs for every image pixel, loaded from 
#the data in template_dir
def load_angles(template_name):
	#Check that template directory exists
	template_dir = path.join(os.getcwd(),'Scan Templates',template_name)
	if(not path.isdir(template_dir)):
		print('Error - Template directory not found:')
		print(template_dir)
		quit(-1)
		
	#Check that files exist
	pitch_angles_file = path.join(template_dir,'pitch_angles.csv')
	yaw_angles_file = path.join(template_dir,'yaw_angles.csv')
	if(not path.isfile(pitch_angles_file) or not path.isfile(yaw_angles_file)):
		print("Error - Corrupt template directory")
		quit(-1)
	
	#Create angle arrays
	yaw_reader = csv.reader(open(yaw_angles_file, "rb"), delimiter=",")
	yaw_angles = np.array(list(yaw_reader)).astype(int)
	pitch_reader = csv.reader(open(pitch_angles_file, "rb"), delimiter=",")
	pitch_angles = np.array(list(pitch_reader)).astype(int)
	
	return np.stack((yaw_angles,pitch_angles),axis=2)