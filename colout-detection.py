import numpy as np
import cv2

cap = cv2.VideoCapture(r'C:\Users\hites\Desktop\robo\opencv_basics\assets\vid (3).mp4')

while True:
    ret, frame = cap.read()
    
    width = int(cap.get(3))#give width of video
    height = int(cap.get(4))#give height of video
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,110,140])
    upper_red = np.array([50,150,210])
    
    mask = cv2.inRange(hsv, lower_red, upper_red) #an image with showing red pixels only, thus took range as lghtest red to darkest blue 
    
    #applying mask over the img
    result = cv2.bitwise_and(frame, frame, mask = mask)# take 2 same frames combine with mask
    
    cv2.imshow('frame', result)
    # cv2.imshow('mask', result) #mask is all binaries 0s, 1s and can be used to apply in imgs
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    
    
#     import numpy as np
# import cv2

# cap = cv2.VideoCapture(r'C:\Users\hites\Desktop\robo\opencv_basics\assets\vid (3).mp4')

# while cap.isOpened():
#     ret, frame = cap.read()
    
#     if not ret:
#         break
    
#     width = int(cap.get(3))#give width of video
#     height = int(cap.get(4))#give height of video
    
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     lower_red = np.array([0,110,140])
#     upper_red = np.array([50,150,210])
    
#     mask = cv2.inRange(hsv, lower_red, upper_red) #an image with showing red pixels only, thus took range as lghtest red to darkest blue 
    
#     #applying mask over the img
#     result = cv2.bitwise_and(frame, frame, mask = mask)# take 2 same frames combine with mask
    
#     cv2.imshow('frame', result)
#     # cv2.imshow('mask', result) #mask is all binaries 0s, 1s and can be used to apply in imgs
#     # Exit the loop when 'q' is pressed
#     if cv2.waitKey(1) == ord('q'):
#         break
    
# # Release the capture and close windows
# cap.release()
# cv
# # Release the capture and close windows
# cap.release()
# cv2.destroyAllWindows()
    