import numpy as np
import cv2

cap = cv2.VideoCapture(r'C:\Users\hites\Desktop\robo\opencv_basics\assets\vid (3).mp4')

import os

video_path = r'C:\Users\hites\Desktop\robo\opencv_basics\assets\vid (3).mp4'
if os.path.exists(video_path):
    print("File exists!")
else:
    print("File not found.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    width = int(cap.get(3))#give width of video
    height = int(cap.get(4))#give height of video
    
    
    #draw lines:
    img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10)# args: the frame, first coordinate, second coordinate, colour of the line, thickmness of the line
    img = cv2.line(img, (0,height), (width, 0), (0, 255, 0), 5)# args: the frame, first coordinate, second coordinate, colour of the line, thickmness of the line

    #rectangle
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), 5)# img, first coordinate top left one, second coordinate bottom right, colour of the the rectangle, thickmness of the rectangle
    
    #circle
    img = cv2.circle(img, (500,500), 60, (255,255,255), -1)#img, center of the circle, diameter, colour, thickmness of the circle
    
    #texts
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Not a basket',(100, height-10), font, 2,(0,0,255), 5, cv2.LINE_AA)#img, txt,coordinate, font, fontscale, colour, thickness, txt_enhancement(optional arg)
    cv2.imshow('frame', img)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    
    
    
# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()