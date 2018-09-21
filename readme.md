## cctv 저장소의 효율을 높여주는 프로그램을 제작하는 프로젝트입니다
### opencv3 의 이미지 프로세싱과 skimage 의 compare_ssim 을 이용하여 알고리즘을 짭니다
### 언어는 파이썬2.7 기준 입니다


### **필요 라이브러리 설치

>pip install numpy  
>python -m pip install opencv-contrib-python  
>pip install --upgrade scikit-image  

#### 절차
**     
#### 1) V01_project.py -> 실행코드  
####    -long_01.mp4,long_01.mp4 -> 테스트 원본파일 ( 실행코드에  input 으로 넣어줍니다 )  
####    -out_01.avi,out_02.avi   -> V01_project.py 를 실행시키면 나오는 output 파일 (수정된 파일) 입니다  
#### output 파일을 확인하려면 cv_02_readVID.py 코드에 output 파일을 input 으로 넣습니다  
  
#### 2) 필요한 부분만 잘 나오는지 확인합니다  
  
#### 3) ls -alh 커맨드를 처서(리눅스) 용량이 얼마나 줄었는지 확인합니다  
**
