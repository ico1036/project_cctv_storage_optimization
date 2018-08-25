# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
 
# load the two input images
imageA = cv2.imread('a1.jpg')
imageB = cv2.imread('a2.jpg')
 
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))
# 1.0  -> perfect matching


