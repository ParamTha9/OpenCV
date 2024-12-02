import numpy as np
import cv2

cap = cv2.VideoCapture(r'vid (3).mp4')

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    width = int(cap.get(3))#give width of video
    height = int(cap.get(4))#give height of video
    
    image = np.zeros(frame.shape, np.uint8)#blank image
    
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE).reshape(540,650,3)#top left
    image[height//2:, :width//2] = smaller_frame#top right
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame#bottom left
    
    #pasting 4 frames in an image by making smaller sized frames
    
    # Display the resulting frame
    cv2.imshow('frame', image)
    
    
    

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()