import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, VideoCapture = cap.read()
    cv2.imshow('VideoCapture', VideoCapture)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()