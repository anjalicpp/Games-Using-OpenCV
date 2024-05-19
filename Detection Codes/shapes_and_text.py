import cv2
import numpy as np

# img = np.zeros((512,512))#zero is for black
# print(img.shape)#o/p:(512,512)==>it is gray image
#Inorder to give it colors we will give it 3 channels
#COLOR TO IMAGE
img = np.zeros((512,512,3),np.uint8)
print(img)

#img[200:300,0:100]=250,0,0#colors only given range as blue
#img[:]=255,0,0#for coloring whole image blue

#TO DRAW A LINE
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#img.shape[1]=width   img.shape[0]=height

#TO DRAW A RECTANGLE BOX
#1.for a rectangle box
cv2.rectangle(img,(0,0),(250,350),(0,0,255),15)
#2.for filled rectangle box
cv2.rectangle(img,(0,0),(250,350),(0,255,0),cv2.FILLED)

#TO DRAW A CIRCLE
cv2.circle(img,(400,50),30,(255,255,0),5)

#TO PUT TEXT ON IMAGE
cv2.putText(img,"OPEN CV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

#to color the image
cv2.imshow("image",img)

cv2.waitKey(0)
