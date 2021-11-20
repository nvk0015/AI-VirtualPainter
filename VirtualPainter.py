from typing import Counter
import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "Header"
listdir = os.listdir(folderPath)

images = []
for img in listdir:
    image = cv2.imread(str(folderPath)+ '/' +str(img))
    images.append(image)
#print(len(images))
header_img = images[0]
#############################
drawColor = (0,0,0)
brushThickness = 15
eraserThickeness = 50
xPrev,yPrev = 0,0
backImg = np.zeros((720,1280,3),np.uint8)
counter = 0
#############################
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.7)
while True:
    #1. Import image
    success, img = cap.read()
    img = cv2.flip(img,1) # user friendly to draw 

    #2. Find HandLmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        #print(lmList)
        x1,y1 = lmList[8][1:] # landmark position for tip of index finger
        x2,y2 = lmList[12][1:] #landmark position for tip of the middle finger


        #3. Check which fingures are up! - One Fingure up
        fingers = detector.fingersUp()
        #print(fingers)


        #4. If selection mode - Two fingures are UP, select the brush/eraser
        if fingers[1] and fingers[2]:
            xPrev,yPrev = 0,0
            print("Selection Mode")
            cv2.rectangle(img,(x1,y1-35),(x2,y2+35),(255,0,255),cv2.FILLED)
            if y1<225:
                if 150<x1<350:
                    header_img=images[0]
                    drawColor = (0,0,255)
                elif 450<x1<650:
                    header_img=images[1]
                    drawColor= (0,255,0)
                elif 700<x1<850:
                    header_img=images[2]
                    drawColor = (255,0,0)
                elif 950<x1<1200:
                    header_img=images[3]
                    drawColor = (0,0,0)
                
                cv2.rectangle(img,(x1,y1-35),(x2,y2+35),drawColor,cv2.FILLED)
            
        #5. Elif Drawing mode - Index Fingure UP, draw the paint on the display
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1,y1),15,(255,0,255),cv2.FILLED)
            print("Drawing Mode")
            if xPrev ==0 and yPrev==0:
                xPrev,yPrev = x1,y1
            if drawColor == (0,0,0):
                cv2.line(img,(xPrev,yPrev),(x1,y1),drawColor,eraserThickeness)
                cv2.line(backImg,(xPrev,yPrev),(x1,y1),drawColor,eraserThickeness)
            else:    
                cv2.line(img,(xPrev,yPrev),(x1,y1),drawColor,brushThickness)
                cv2.line(backImg,(xPrev,yPrev),(x1,y1),drawColor,brushThickness)
            xPrev,yPrev = x1,y1
    
    # imgGray = cv2.cvtColor(backImg,cv2.COLOR_BGR2GRAY)
    # ret,imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    # imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    # img = cv2.bitwise_and(img,imgInv)
    # img = cv2.bitwise_or(img,backImg)

    #setting the header image
    img[0:125,0:1280] = header_img
    img = cv2.addWeighted(img,0.5,backImg,0.5,0)
    key = cv2.waitKey(1)
    cv2.imshow('WebCam', img)
    cv2.imshow('AI Painter',backImg)
    #cv2.imshow('Krones AI Painter',imgInv)
    if key == 27:
        cv2.imwrite("SavedImages/Painter"+str(counter)+".jpg",backImg)
        counter +=1
        break
cv2.destroyAllWindows()