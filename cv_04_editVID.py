#-*-coding:utf-8-*-

import numpy as np
import cv2

def showVideo():
	
	cap = cv2.VideoCapture('videos/test3.mp4')
	

	fps=20.0
	width  = int(cap.get(3))
	height = int(cap.get(4))

	fcc = cv2.VideoWriter_fourcc('D','I','V','X')
	out = cv2.VideoWriter('sample1.avi', fcc, fps, (width,height))

	

	CurrentFrame=0
	StartFrame=150
	EndFrame=151
	# 현재 프레임 계산에 이용할 CurrentFrame
	# 시작 프레임 설정 StartFrame 
	# 종료 프레임 설정 EndFrame

	cap.set(cv2.CAP_PROP_POS_FRAMES,StartFrame)
	#설정한 시작프레임으로 영상 시작점을 조정합니다
	CurrentFrame=StartFrame
	#현재 프레임을 시작 프레임으로 설정합니다
	print('녹화를 시작합니다')

	while True:
		ret, frame = cap.read()
		if not ret:
			print("read error")
			break
			
		cv2.imshow('video', frame)
		out.write(frame)
		#녹화와 출력은 동시에 이루어집니다		
		#cv2.imwrite("ExtIMG%d.jpg" % CurrentFrame,frame) 
		#캡처기능

		CurrentFrame+=1
		#영상이 녹화되고 그다음 현재 프레임이 올라갑니다

		k =cv2.waitKey(1) & 0xFF
		if k == 27 or CurrentFrame==EndFrame :
			print('녹화를 종료합니다')
			print('start: ',StartFrame,'end: ', CurrentFrame)
			break
		#현재 프레임이 설정한 종료프레임과 같아지면 녹화를 종료합니다
	cap.release()
	out.release()
	cv2.dsetroyAllWindows()


showVideo()
