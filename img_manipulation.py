import cv2
import random

img = cv2.imread(r'C:\Users\hites\Desktop\robo\opencv_basics\assets\Ball.png', -1)

print(img) #prints numpy arrays

print(type(img))
print(img.shape) #height, width, channels(BGR in case of opencv)

#1st row of image
# print(img[0][700:800])#range of pixels in img row of pixels

#changing pixels:
for i in range(100):
    for j in range(img.shape[1]):#1st row of image
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

