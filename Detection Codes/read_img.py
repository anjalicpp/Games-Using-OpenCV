import cv2
import os
print("reading image video and webcam demo")


# print("reading image:")
# img = cv2.imread(f'{"Resources"}/{"box8_image.jpg"}')#reading image from folder Resources

# cv2.imshow("output",img)#(windowname,image_to_be_displayed)
# #to hold output screen we give delay with cv2.wait(time_in_milisec)
# cv2.waitKey(0)#infinite wait

# print("reading a video:")

# cap = cv2.VideoCapture("Resources\[Kayoanime] - S01E01 (001).mkv")
# # a video is sequence of images so we need a while loop to output the video
# while True:
#     success,img = cap.read()#read video in img variable and success tells whether the task was successful or not
#     #sucess is boolean variable-->avlues are true or false
#     cv2.imshow("Video",img)
    
#     if cv2.waitKey(1) & 0xFF ==ord('q'):#gives delay and when 'q' is pressed window is disolved
#         break
    
print("reading from a webcam:")
#same as video reading just change path
cap = cv2.VideoCapture(0)
#change the path==>0 uses default webcam and define parameters for window size
cap.set(3,640)#width_id=3,widthsize
cap.set(4,480)#height_id=4,heightsize
cap.set(10,100)#to set brightness more id=10

while True:
    success,img = cap.read()#read video in img variable and success tells whether the task was successful or not
    #sucess is boolean variable-->avlues are true or false
    cv2.imshow("Video",img)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):#gives delay and when 'q' is pressed window is disolved
        break
    
    
     
