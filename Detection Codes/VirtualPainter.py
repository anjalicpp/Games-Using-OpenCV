# import cv2
# import numpy as np
# import time 
# import os 
# import HandTrackingModule as htm
# import pygame
# from flask import Blueprint, render_template
# from tensorflow.keras.models import load_model
# import keyboard

# VirtualPainter = Blueprint("HandTrackingModule", __name__, static_folder="static",template_folder="templates")

# @VirtualPainter.route("/feature")

# def strt():
#     ##############
#     brushThickness = 15
#     eraserThickness = 100
#     width, height = 1280, 720
# #############
# #PYGAME ATTRIBUTES
#     pygame.init()
#     FONT = pygame.font.SysFont('freesansbold.tff', 18)
#     DISPLAYSURF = pygame.display.set_mode((width, height),flags=pygame.HIDDEN)
#     pygame.display.set_caption("Digit Board")
#     number_xcord = []
#     number_ycord = []
########################
    




# # Load the Models
#     AlphaMODEL = load_model("DevNagri_prediction_model.h5")
#     AlphaLABELS = {0: u'\u091E', 1: u'\u091F', 2: u'\u0920', 3: u'\u0921', 4: u'\u0922', 5: u'\u0923', 6: u'\u0924', 7: u'\u0925', 8: u'\u0926', 9: u'\u0927', 10: u'\u0915', 11: u'\u0928', 12: u'\u092A', 13: u'\u092B', 14: u'\u092c', 15: u'\u092d', 16: u'\u092e', 17: u'\u092f', 18: u'\u0930', 19: u'\u0932', 20: u'\u0935', 21: u'\u0916', 22: u'\u0936', 23: u'\u0937', 24: u'\u0938', 25: u'\u0939', 26: 'ksha', 27: 'tra', 28: 'gya', 29: u'\u0917', 30: u'\u0918', 31: u'\u0919', 32: u'\u091a', 33: u'\u091b', 34: u'\u091c', 35: u'\u091d', 36: u'\u0966', 37: u'\u0967', 38: u'\u0968', 39: u'\u0969', 40: u'\u096a', 41: u'\u096b', 42: u'\u096c', 43: u'\u096d', 44: u'\u096e', 45: u'\u096f'}

# #############
# # Initialize Prediction Variables
#     label = ""
#     PREDICT = "alpha"
#     rect_min_x, rect_max_x = 0, 0
#     rect_min_y, rect_max_y = 0, 0
#     number_xcord, number_ycord = [], []


#     folderPath = "Header"
#     myList = os.listdir(folderPath)
#     print(myList)

#     overlayList = []

#     for imPath in myList:
#         image = cv2.imread(f'{folderPath}/{imPath}')
#         overlayList.append(image)
#     print(len(overlayList))

#     header = overlayList[0]
#     drawColor = (255,0,255)
# #########cv2Attributes##############
#     cap = cv2.VideoCapture(0)
#     cap.set(3,1280)
#     cap.set(4,720)

#     detector = htm.handDetector(detectionCon=0.85)

#     xp,yp = 0, 0
#     modeValue = "OFF"
#     modeColor = RED
#     imgCanvas = np.zeros((728,1280,3),np.uint8)#drawing a canvas with numpy
# ##########################

#     while True:
#     #1.Import the Image
#         success, img = cap.read()
#         img = cv2.flip(img,1)#flipping img so it move same as us on webcam
    
    
#     #2.Find Hand landmarks
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img, draw=False)
    
    
#     #-->
#         print("Reched Virtual paint module")
#         cv2.putText(img,"Press N for HINDI CHARCTER Recognisition Mode ",(0,162),3,0.5,(255,255,0),1,cv2.LINE_AA)
#         cv2.putText(img,"Press O for Turn Off Recognisition Mode ",(0,179),3,0.5,(255,255,0),1,cv2.LINE_AA)
#         cv2.putText(img,f'{"RECOGNISITION IS "}{modeValue}',(0,196),3,0.5,modeColor,1,cv2.LINE_AA)

#         if keyboard.is_pressed('a'):
#             if PREDICT!="alpha":
#                 PREDICT = "alpha"
#                 modeValue, modeColor = "ALPHABATES", GREEN
            
#         if keyboard.is_pressed('o'):
#             if PREDICT!="off":
#                 PREDICT = "off"
#                 modeValue, modeColor = "OFF", RED
        
#             xp , yp = 0, 0
#             label=""
#             rect_min_x, rect_max_x = 0,0
#             rect_min_y, rect_max_y = 0,0
#             number_xcord = []
#             number_ycord = []
#             time.sleep(0.5)
        
    
#         if len(lmList)!=0:
#         #print(lmList)
        
#         #tip of index and middle finger
#             x1,y1 = lmList[8][1:]#index finger
#             x2,y2 = lmList[12][1:]
        
#         #3.Check which finger is up:we want to draw with index finger and for selction use two fingers
#             fingers = detector.fingersUp()
#         #print(fingers)
    
#     #4.If Selection mode-Two fingers are up
#             if fingers[1] and fingers[2]:
#                 number_xcord = sorted(number_xcord)
#                 number_ycord = sorted(number_ycord)

#                 if(len(number_xcord) > 0 and len(number_ycord)>0 and PREDICT!="off"):
#                     if drawColor!=(0,0,0) and lastdrawColor != (0,0,0):
#                         rect_min_x, rect_max_x = max(number_xcord[0]-BOUNDRYINC, 0), min(width, number_xcord[-1]+BOUNDRYINC)
#                         rect_min_y, rect_max_y = max(0, number_ycord[0]-BOUNDRYINC), min(number_ycord[-1]+BOUNDRYINC, height)
#                         number_xcord = []
#                         number_ycord = []

#                         img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_x,rect_min_y:rect_max_y].T.astype(np.float32) 

#                         cv2.rectangle(imgCanvas,(rect_min_x,rect_min_y),(rect_max_x,rect_max_y),BORDER,3)
#                         image = cv2.resize(img_arr, (32,32))
#                         # cv2.imshow("Tmp",image)
#                         image = np.pad(image, (10,10), 'constant' , constant_values =0)
#                         image = cv2.resize(image,(32,32))/255
#                     # cv2.imshow("Tmp",image)
                        
#                         if PREDICT == "alpha":
#                             label = str(AlphaLABELS[np.argmax(AlphaMODEL.predict(image.reshape(1,32,32,1)))])
#                         pygame.draw.rect(DISPLAYSURF,BLACK,(0,0,width,height))

#                         cv2.rectangle(imgCanvas,(rect_min_x+50,rect_min_y-20),(rect_min_x,rect_min_y),BACKGROUND,-1)
#                         cv2.putText(imgCanvas,label,(rect_min_x,rect_min_y-5),3,0.5,FORGROUND,1,cv2.LINE_AA)
                
#                     else:
#                         number_xcord = []
#                         number_ycord = []
            
#                 xp,yp = 0,0
            
#                 print("Selection Mode")
#             #Check for click
#                 if y1 < 125:
#                     if 250 <x1< 450:
#                         header = overlayList[0]
#                         drawColor = (255,0,255)#purple
#                     elif 550 <x1< 750:
#                         header = overlayList[1]
#                         drawColor = (255,0,0)#Blue
#                     elif 800 <x1< 950:
#                         header = overlayList[2]
#                         drawColor = (0,255,0)#green
#                     elif 1050 <x1< 1200:
#                         header = overlayList[3]
#                         drawColor = (0,0,0)#black
#                 cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)
                        
            
            
#     #5.If Drawing mode-Index finger is up
#             elif fingers[1] and fingers[2]==False:
#                 number_xcord.append(x1)
#                 number_ycord.append(y1)
                
                
#                 cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
#                 print("Drawing Mode")
                
#                 if(xp==0 and yp==0):#veryf first frame case
#                     xp, yp = x1, y1 
                    
#                 if drawColor==(0,0,0):
#                     cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
#                     cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                
#                 else:
#                     cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
#                     cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
#                     pygame.draw.line(DISPLAYSURF, WHITE, (xp,yp), (x1,y1), brushThickness)
#                 xp,yp = x1,y1
#             else:
#                 xp,yp   = 0,0
        
#         imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
#         _, imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
        
#         imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
#         #result = cv2.bitwise_and(img, imgInv_resized)
        
#         imgInv_resized = cv2.resize(imgInv, (img.shape[1], img.shape[0]))
        
#         img = cv2.bitwise_and(img,imgInv_resized)
        
        
#         imgCanvas_resized = cv2.resize(imgCanvas, (img.shape[1], img.shape[0]))

#         img = cv2.bitwise_or(img,imgCanvas_resized)
        
#         #Setting header image
#         img[0:125,0:1280] = header#at coordinates 0-125 width and 0-1280 height we will overlay header image
#         #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)#overlaping canvas and original img
#         pygame.display.update()
#         cv2.imshow("Image",img)
        
#         #cv2.imshow("Canvas",imgCanvas)
#         #cv2.imshow("Inv",imgInv_resized)
        
#         #cv2.waitKey(1)
#         cv2.waitKey(1)

#     strt() 


#VirtualPaint
import cv2
import numpy as np
import time 
import os 
import HandTrackingModule as htm
import pygame
from flask import Blueprint, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import keyboard

VirtualPainter = Blueprint("HandTrackingModule", __name__, static_folder="static",template_folder="templates")

@VirtualPainter.route("/feature")

def strt():
    ##############
    brushThickness = 10
    eraserThickness = 100
    width, height = 1280, 720
#############
#PYGAME ATTRIBUTES
    pygame.init()
    FONT = pygame.font.SysFont('freesansbold.tff', 18)
    DISPLAYSURF = pygame.display.set_mode((width, height),flags=pygame.HIDDEN)
    pygame.display.set_caption("Digit Board")
    number_xcord = []
    number_ycord = []
############


# Load the Models
    AlphaMODEL = load_model("DevNagri_prediction_model.h5")
    AlphaLABELS = {0: u'\u091E', 1: u'\u091F', 2: u'\u0920', 3: u'\u0921', 4: u'\u0922', 5: u'\u0923', 6: u'\u0924', 7: u'\u0925', 8: u'\u0926', 9: u'\u0927', 10: u'\u0915', 11: u'\u0928', 12: u'\u092A', 13: u'\u092B', 14: u'\u092c', 15: u'\u092d', 16: u'\u092e', 17: u'\u092f', 18: u'\u0930', 19: u'\u0932', 20: u'\u0935', 21: u'\u0916', 22: u'\u0936', 23: u'\u0937', 24: u'\u0938', 25: u'\u0939', 26: 'ksha', 27: 'tra', 28: 'gya', 29: u'\u0917', 30: u'\u0918', 31: u'\u0919', 32: u'\u091a', 33: u'\u091b', 34: u'\u091c', 35: u'\u091d', 36: u'\u0966', 37: u'\u0967', 38: u'\u0968', 39: u'\u0969', 40: u'\u096a', 41: u'\u096b', 42: u'\u096c', 43: u'\u096d', 44: u'\u096e', 45: u'\u096f'}

#############
# Initialize Prediction Variables
    label = " "
    PREDICT = "off"
    rect_min_x, rect_max_x = 0, 0
    rect_min_y, rect_max_y = 0, 0
    number_xcord, number_ycord = [], []


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
    
#####COLOR ATTRIBUTES#########
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    RED = (0,0,255)
    YELLOW = (0,255,255)
    GREEN = (0,255,0)
    BACKGROUND = (255,255,255)
    FORGROUND = (0,255,0)
    BORDER = (0,255,0)
    lastdrawColor = (0,0,1)
    drawColor = (0,0,255)
    BOUNDRYINC = 5
#############################
#########cv2Attributes##############
    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)

    detector = htm.handDetector(detectionCon=0.85)

    xp,yp = 0, 0
    
  
    modeValue = "none"
    modeColor = RED
    imgCanvas = np.zeros((728,1280,3),np.uint8)#drawing a canvas with numpy

##########################################
    while True:
    #1.Import the Image
        success, img = cap.read()
        img = cv2.flip(img,1)#flipping img so it move same as us on webcam
    
    
    #2.Find Hand landmarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
    
    
    #-->
        #print("Reched Virtual paint module")
        cv2.putText(img,"Press A for HINDI CHARCTER Recognisition Mode ",(0,162),3,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(img,"Press O for Turn Off Recognisition Mode ",(0,179),3,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.putText(img,f'{"RECOGNISITION IS "}{modeValue}',(0,196),3,0.5,modeColor,1,cv2.LINE_AA)
        cv2.putText(img,f'{"PREDICTION MODE IS "}{PREDICT}',(0,212),3,0.5,(255,255,0),1,cv2.LINE_AA)
        
        #print("keyboard press wali line debugg:")
        if keyboard.is_pressed('a'):
            keyboard.release('a')
            if PREDICT!="alpha":
                PREDICT = "alpha"
                print("alpha mode wala block--------->")
                modeValue, modeColor = "ALPHABATES", GREEN
            time.sleep(1)
            
        if keyboard.is_pressed('o'):
            
            if PREDICT!="off":
                print("keyboard se o press wala block")
                PREDICT = "off"
                modeValue, modeColor = "OFF", RED
        
            print("Bhar aa gya hu")
            xp , yp = 0, 0
            label=""
            rect_min_x, rect_max_x = 0,0
            rect_min_y, rect_max_y = 0,0
            number_xcord = []
            number_ycord = []
            time.sleep(0.5)
        
    
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
                number_xcord = sorted(number_xcord)
                number_ycord = sorted(number_ycord)

                if(len(number_xcord) > 0 and len(number_ycord)>0 and PREDICT!="off"):
                    if drawColor!=(0,0,0) and lastdrawColor != (0,0,0):
                        rect_min_x, rect_max_x = max(number_xcord[0]-BOUNDRYINC, 0), min(width, number_xcord[-1]+BOUNDRYINC)
                        rect_min_y, rect_max_y = max(0, number_ycord[0]-BOUNDRYINC), min(number_ycord[-1]+BOUNDRYINC, height)
                        number_xcord = []
                        number_ycord = []

                        img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_x,rect_min_y:rect_max_y].T.astype(np.float32) 

                        cv2.rectangle(imgCanvas,(rect_min_x,rect_min_y),(rect_max_x,rect_max_y),BORDER,3)
                        image = cv2.resize(img_arr, (32,32))
                        
                       
                        
                        
                        cv2.imshow("Tmp1",image)
                        #image = np.pad(image, (10,10), 'constant' , constant_values =0)
                        #image = cv2.resize(image,(32,32))/255
                        image = image.astype("float")/255.0
                        cv2.imshow("Tmp2",image)
                        
                                              
                        
                        if PREDICT == "alpha":
                            print("**************************model prediction wali line***********************************")
                            # image = image.reshape(1,32,32,1)
                            # label = AlphaLABELS[np.argmax(AlphaMODEL.predict(image)[0])]
                            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                            image = img_to_array(image)
                            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                            image = np.expand_dims(image, axis=0)
                            image = np.expand_dims(image, axis=3)
                            
                            lists = AlphaMODEL.predict(image)[0]
                            print("The letter is ",AlphaLABELS[np.argmax(lists)])
                            label=str(AlphaLABELS[np.argmax(lists)])
                        pygame.draw.rect(DISPLAYSURF,BLACK,(0,0,width,height))

                        cv2.rectangle(imgCanvas,(rect_min_x+50,rect_min_y-20),(rect_min_x,rect_min_y),BACKGROUND,-1)
                        cv2.putText(imgCanvas,label,(rect_min_x,rect_min_y-5),3,0.5,FORGROUND,1,cv2.LINE_AA)
                
                    else:
                        number_xcord = []
                        number_ycord = []
            
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
            elif fingers[1] and fingers[2]==False:
                number_xcord.append(x1)
                number_ycord.append(y1)
                
                
                cv2.circle(img,(x1,y1-15),15,drawColor,cv2.FILLED)
                print("Drawing Mode")
                
                if(xp==0 and yp==0):#veryf first frame case
                    xp, yp = x1, y1 
                    
                if drawColor==(0,0,0):
                    cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                    cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                
                else:
                    cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                    cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
                    pygame.draw.line(DISPLAYSURF, WHITE, (xp,yp), (x1,y1), brushThickness)
                xp,yp = x1,y1
            else:
                xp,yp   = 0,0
        
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
        pygame.display.update()
        cv2.imshow("Image",img)
        
        #cv2.imshow("Canvas",imgCanvas)
        #cv2.imshow("Inv",imgInv_resized)
        
        #cv2.waitKey(1)
        cv2.waitKey(1)

    strt() 