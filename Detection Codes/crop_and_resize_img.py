import cv2
import numpy as np

img = cv2.imread("Resources/box8_image.jpg")
print(img.shape)#printing original image shape and dimensions o/p:(608, 758, 3)


#resize The Image
imgResize = cv2.resize(img,(300,200))#(width,height)
print(imgResize.shape)

#imageCropping
imgCropped = img[0:100,200:300]#(height,width)

cv2.imshow("Image",img)
cv2.imshow("Image_resize",imgResize)
cv2.imshow("image_croppped",imgCropped)


cv2.waitKey(0)
