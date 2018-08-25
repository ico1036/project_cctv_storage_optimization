#-*-coding:utf-8-*-
# KOREAN 

import numpy as np
import cv2

def showImage():
	imgfile = 'images/test01.jpg'
	img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
#imread: 이미지 파일을 읽기 위한 객체를 리턴 
	#형식: imread(읽고자 하는 이미지파일경로,이미지파일 읽는 방식)
	#이미지 파일 읽는 방식(이미지플래그) 
		#IMREAD_COLOR: 컬러이미지,투명무시,티폴트플래그, 정수값:1
		#IMREAD_GRAYSCALE: 흑백, 정수값:0
		#IMREAD_UNCHANGED: 알파채널을 포함하여 이미지를 그대로, 정수값:-1
	print(img)
	print(type(img))
	print(img.shape)
#이미지 객체는 NumPy array type으로 구성되어있다
	cv2.imshow('model' , img)
#imshow: 이미지 객체를 화면에 나타냄 (윈도우타이틀,이미지객체)

	k = cv2.waitKey(0) & 0xFF
# 0xFF: 64bit 운영체제

	if k ==27:
		cv2.destroyAllWindows()
	elif k==ord('c'):
		cv2.imwrite('copy.jpg',img)
		cv2.destroyAllWindows()
		
# 화면에 이미지를 표시한 후
# ESC 를 누르면 종료, c 를 누르면 복사

showImage()

