#-*-coding:utf-8-*-

import numpy as np
import cv2

def showVideo():
	
	cap = cv2.VideoCapture('videos/test3.mp4')
	

	fps=20.0
	# frame 속도를 지정한다
	width  = int(cap.get(3))
	height = int(cap.get(4))
	# 기존 영상의 높이와 너비를 사용한다

	fcc = cv2.VideoWriter_fourcc('D','I','V','X')
	# DIVX코덱을 적용한다 
	out = cv2.VideoWriter('sample.avi', fcc, fps, (width,height))
	# 비디오 저장을 위한 객체

	
	print('녹화를 시작합니다')

	while True:
		ret, frame = cap.read()
		# 재생되는 비디오를 한 frame씩 읽는다
		# 정상적으로 읽을 시 ret 변수에  True 가 들어간다
		if not ret:
			print("read error")
			break
		cv2.imshow('video', frame)
		out.write(frame)
		k =cv2.waitKey(1) & 0xFF
		if k == 27:
			print('녹화를 종료합니다')
			break
	
	cap.release()
	out.release()
	cv2.dsetroyAllWindows()


showVideo()
