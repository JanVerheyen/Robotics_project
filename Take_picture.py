import cv2
import imutils

def rotate_image(image):
    rotated = imutils.rotate_bound(image, 180)
    return rotated

def take_picture():    
    cap = cv2.VideoCapture(0)
    ramp_frames = 30
    
    ret, frame = cap.read()
    
    for i in range(ramp_frames):
        ret, temp = cap.read()
    
    ret, frame = cap.read()
    
    frame = rotate_image(frame)
    
    cv2.imwrite('Pictures/test.png',frame)
    
    # Release everything if job is finished
    cap.release() 