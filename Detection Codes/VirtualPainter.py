import cv2
import numpy as np
import os
import HandTrackingModule as htm
from tensorflow.keras.models import load_model

##############
brushThickness = 15
eraserThickness = 100
##############

# Load the Models
AlphaMODEL = load_model("DevNagri_prediction_model.h5")
AlphaLABELS = {0: u'\u091E', 1: u'\u091F', 2: u'\u0920', 3: u'\u0921', 4: u'\u0922', 5: u'\u0923', 6: u'\u0924', 7: u'\u0925', 8: u'\u0926', 9: u'\u0927', 10: u'\u0915', 11: u'\u0928', 12: u'\u092A', 13: u'\u092B', 14: u'\u092c', 15: u'\u092d', 16: u'\u092e', 17: u'\u092f', 18: u'\u0930', 19: u'\u0932', 20: u'\u0935', 21: u'\u0916', 22: u'\u0936', 23: u'\u0937', 24: u'\u0938', 25: u'\u0939', 26: 'ksha', 27: 'tra', 28: 'gya', 29: u'\u0917', 30: u'\u0918', 31: u'\u0919', 32: u'\u091a', 33: u'\u091b', 34: u'\u091c', 35: u'\u091d', 36: u'\u0966', 37: u'\u0967', 38: u'\u0968', 39: u'\u0969', 40: u'\u096a', 41: u'\u096b', 42: u'\u096c', 43: u'\u096d', 44: u'\u096e', 45: u'\u096f'}

# Initialize Prediction Variables
label = ""
PREDICT = "alpha"
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
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.85)

xp, yp = 0, 0
imgCanvas = np.zeros((728, 1280, 3), np.uint8)  # Drawing a canvas with numpy

while True:
    # 1. Import the Image
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flipping img so it moves same as us on webcam

    # 2. Find Hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList)

        # Tip of index and middle finger
        x1, y1 = lmList[8][1:]  # Index finger
        x2, y2 = lmList[12][1:]

        # 3. Check which finger is up: we want to draw with index finger and for selection use two fingers
        fingers = detector.fingersUp()
        # print(fingers)

        # 4. If Selection mode - Two fingers are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0

            print("Selection Mode")
            # Check for click
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)  # Purple
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)  # Blue
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)  # Green
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)  # Black
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing mode - Index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp == 0 and yp == 0:  # Very first frame case
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            number_xcord.append(x1)
            number_ycord.append(y1)
            xp, yp = x1, y1

        if fingers[1] == False and fingers[2] == False and len(number_xcord) > 0:
            number_xcord = sorted(number_xcord)
            number_ycord = sorted(number_ycord)
            rect_min_x, rect_max_x = max(number_xcord[0] - 5, 0), min(1280, number_xcord[-1] + 5)
            rect_min_y, rect_max_y = max(number_ycord[0] - 5, 0), min(720, number_ycord[-1] + 5)
            number_xcord, number_ycord = [], []

            img_arr = imgCanvas[rect_min_y:rect_max_y, rect_min_x:rect_max_x]
            img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
            img_arr = cv2.resize(img_arr, (28, 28))
            img_arr = img_arr / 255.0

            if PREDICT == "alpha":
                prediction = AlphaMODEL.predict(img_arr.reshape(1, 32, 32, 1))
                label = AlphaLABELS[np.argmax(prediction)]

            cv2.rectangle(imgCanvas, (rect_min_x, rect_min_y - 20), (rect_min_x + 50, rect_min_y), (255, 255, 255), -1)
            cv2.putText(imgCanvas, label, (rect_min_x, rect_min_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)

    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    imgInv_resized = cv2.resize(imgInv, (img.shape[1], img.shape[0]))

    img = cv2.bitwise_and(img, imgInv_resized)

    imgCanvas_resized = cv2.resize(imgCanvas, (img.shape[1], img.shape[0]))

    img = cv2.bitwise_or(img, imgCanvas_resized)

    # Setting header image
    img[0:125, 0:1280] = header  # At coordinates 0-125 width and 0-1280 height we will overlay header image
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Inv", imgInv_resized)

    cv2.waitKey(1)
