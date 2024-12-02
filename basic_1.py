import cv2

# load image
img = cv2.imread(r'C:\Users\hites\Desktop\robo\opencv_basics\assets\Ball.png', 0)
'''
0 for grayscale
-1 for BGR: default: without transpaarency
1 for BGR with alpha channel, i.e with transparency
'''

# img = cv2.resize(img, (400, 400)) : a particaular dimension
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)#half the size

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#default load by cv2 in form of BGR 

cv2.imwrite('changed_img.jpg', img)

cv2.imshow('diplay_window', img)#display window name, image
cv2.waitKey(0)#wait until key pressed, if any other no. then that many secs
cv2.destroyAllWindows()