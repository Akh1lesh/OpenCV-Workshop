import cv2
import numpy
print('hello')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
area = []
p=0
q=0
r=0
while True:
    
    success, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.1,2)
    for(x,y,w,h) in face:
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        # area.append(w*h)
        if((w*h)>=p):
            p = w*h
            q = w
            r = h
            cv2.rectangle(frame,(x,y),(x+q,y+r),(0,255,0),5)
            print(p)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
# print(max(area));

cap.release()

