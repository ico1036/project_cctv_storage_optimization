import cv2
import os
import glob
from skimage.measure import compare_ssim
import matplotlib.pyplot as plt
import numpy as np

f = open("results_name.txt", 'w')

img_dir = "images"
data_path = os.path.join(img_dir,'*jpg')
files = glob.glob(data_path)
data = []
a=0

print files

for f1 in files:
	if f1==1:
		img = cv2.imread(f1)
		data.append(img)
		a=a+1
		cprimg=img
    	continue

	if not f1==1:
		img = cv2.imread(f1)


		if compare_ssim(img,cprimg)>0.90: 
			data.append(img)
			a=a+1
			print(compare_ssim(img,cprimg))
    
	cprimg=img

a=int(a)

for i in range(1, a):
	z=data[i-1]
	f.write(z)

f.close()
