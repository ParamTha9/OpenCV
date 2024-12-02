import numpy as np
import cv2

img = cv2.imread(r'C:\Users\hites\Desktop\robo\opencv_basics\assets\Ball.png')
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75) #img is large so resize it

#while such algos work in grayscale convert it into grayscale format

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#algo: Shitomashi corner detector
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 1) #img, 100 best, corner quality(range: 0-1), closeness/min eucl-dist between corners
#the above will return array of float points
# print(type(corners))

corners = np.int8(corners)#converting float to ints

for corner in corners:
    x,y = corner.ravel()# flatens the array to single array
    cv2.circle(gray, (x,y), 5, (255,0,0), -1)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





