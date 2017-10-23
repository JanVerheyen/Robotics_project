import cv2

def take_picture():    
    cap = cv2.VideoCapture(2)
    ramp_frames = 30
    
    ret, frame = cap.read()
    
    for i in range(ramp_frames):
        ret, temp = cap.read()
    
    ret, image = cap.read()

    frame = image[46:440,118:520]
    
    cv2.imwrite('Pictures/test15.png',frame)
    
    # Release everything if job is finished
    cap.release()
