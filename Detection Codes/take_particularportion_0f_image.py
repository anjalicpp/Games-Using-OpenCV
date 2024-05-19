import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])#to take out a particuar portion we needs its coordinates
#These pixel coordinates can be found out usinf mspaint
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])#to take the particular portion into image 
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("output",imgOutput)

cv2.waitKey(0)
