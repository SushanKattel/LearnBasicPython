import cv2
cap = cv2.VideoCapture(0)
ret,frame = cap.read()
while(True):
    cv2.imshow('img1',frame)
    cv2.imwrite('thepicture.jpg',frame)
    cv2.destroyAllWindows()
    break
cap.release()