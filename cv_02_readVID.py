#-*-coding:utf-8-*-

import numpy as np
import cv2

def showVideo():
	
	cap = cv2.VideoCapture('/home/jkim/gitdir/project_cctv_storage_optimization/out_01.avi')
	#비디오객체를 반환한다

	cap.set(3,480)
	cap.set(4,320)

	#cap.set(cv2.CAP_PROP_POS_FRAMES,300)
    # 원하는 프레임으로 이동할 수 있다




	while True:
		ret, frame = cap.read()
		# 재생되는 비디오를 한 frame씩 읽는다
		# 정상적으로 읽을 시 ret 변수에  True 가 들어간다
		if not ret:
			print("read error")
			break
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('video', gray)

		k =cv2.waitKey(1) & 0xFF
		if k == 27:
			break
	
	cap.release()
	#open 한 cap 객체를 해제한다
	cv2.dsetroyAllWindows()


showVideo()
