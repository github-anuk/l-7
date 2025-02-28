import cv2
import numpy as np
import time
 

#Algorithm
#1. Capture and store the background frame [ This will be done for some seconds ]
#2. Detect the red colored cloth using color detection and segmentation algorithm.
#3. Segment out the red colored cloth by generating a mask. [ used in code ]
#4. Generate the final augmented output to create a magical effect. [ video.mp4 ]


raw_video=cv2.VideoCapture(0)

time.sleep(1)
count = 0
background = 0

for i in range (60):
    return_value,background=raw_video.read()
    if return_value == False:
        continue 


background = np.flip(background,axis = 1)
while(raw_video.isOpened()):
    return_value,img = raw_video.read()
    if not return_value:
        break
    count = count+1
    img=np.flip(img,axis = 1) 
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #maskkk1111
    lower_red=np.array([100,40,40])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    # massssssk2
    lower_red=np.array([155,40,40])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1=mask1+mask2
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8),iterations = 2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
    mask2= cv2.bitwise_not(mask1)
    

    res1=cv2.bitwise_and(background,background,mask = mask1)
    res2=cv2.bitwise_and(img,img,mask= mask2)
    final_output=cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("INSVISBLE CASE",final_output)

    k=cv2.waitKey(10)
    if k == 27:
        break


