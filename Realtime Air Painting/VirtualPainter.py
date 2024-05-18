import cv2
import numpy as np
import time 
import os 
import HandTrackingModule as htm

##############
brushThickness = 15
eraserThickness = 100
#############


folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)

overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
drawColor = (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)

xp,yp = 0, 0
imgCanvas = np.zeros((728,1280,3),np.uint8)#drawing a canvas with numpy

while True:
    #1.Import the Image
    success, img = cap.read()
    img = cv2.flip(img,1)#flipping img so it move same as us on webcam
    
    
    #2.Find Hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList)!=0:
        #print(lmList)
        
        #tip of index and middle finger
        x1,y1 = lmList[8][1:]#index finger
        x2,y2 = lmList[12][1:]
        
        
    
    
    #3.Check which finger is up:we want to draw with index finger and for selction use two fingers
        fingers = detector.fingersUp()
        #print(fingers)
    
    #4.If Selection mode-Two fingers are up
        if fingers[1] and fingers[2]:
            xp,yp = 0,0
            
            print("Selection Mode")
            #Check for click
            if y1 < 125:
                if 250 <x1< 450:
                    header = overlayList[0]
                    drawColor = (255,0,255)#purple
                elif 550 <x1< 750:
                    header = overlayList[1]
                    drawColor = (255,0,0)#Blue
                elif 800 <x1< 950:
                    header = overlayList[2]
                    drawColor = (0,255,0)#green
                elif 1050 <x1< 1200:
                    header = overlayList[3]
                    drawColor = (0,0,0)#black
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)
                    
            
            
    #5.If Drawing mode-Index finger is up
        if fingers[1] and fingers[2]==False:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            print("Drawing Mode")
            if(xp==0 and yp==0):#veryf first frame case
                xp, yp = x1, y1 
                
            if drawColor==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
            
            else:
                cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
            
            xp,yp = x1,y1
    
    imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    #result = cv2.bitwise_and(img, imgInv_resized)
    
    imgInv_resized = cv2.resize(imgInv, (img.shape[1], img.shape[0]))
    
    img = cv2.bitwise_and(img,imgInv_resized)
    
    
    imgCanvas_resized = cv2.resize(imgCanvas, (img.shape[1], img.shape[0]))

    img = cv2.bitwise_or(img,imgCanvas_resized)
    
    #Setting header image
    img[0:125,0:1280] = header#at coordinates 0-125 width and 0-1280 height we will overlay header image
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)#overlaping canvas and original img
    cv2.imshow("Image",img)
    cv2.imshow("Canvas",imgCanvas)
    cv2.imshow("Inv",imgInv_resized)
    
    #cv2.waitKey(1)
    cv2.waitKey(1)
     