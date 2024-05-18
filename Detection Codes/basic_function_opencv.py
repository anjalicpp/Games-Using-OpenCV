import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)#kernel is set of matrix,size=5X5,bit values 2^8=256
img = cv2.imread("Resources/box8_image.jpg")
#cvtColor is used to change the color of image :for colored image we use convention BGR in opencv


#1.for converting imag into gray image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray_image",imgGray)


#2.for converting to BlurImage
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)#kernelsize=(7,7)it is always odd numbers


#3.for edges in image
imgCanny = cv2.Canny(img,100,100)#threshold values 100,100

#4.for dilation:sometimes for detecting image we need to dilate the edges in gaps
imgDilation = cv2.dilate(imgCanny,kernel,iterations =1)

#5.Erosion
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow("Blur_Image",imgBlur)
cv2.imshow("Gray_image",imgGray)
cv2.imshow("Canny_Image",imgCanny)
cv2.imshow("Dilated_image",imgDilation)
cv2.imshow("Eroded_image",imgEroded)

cv2.waitKey(0)
