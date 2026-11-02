import cv2
import datetime


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('no camera')
    exit()

while True:
    v, image = cap.read()

    if not v:
        print('no cadr')
        break

    date = datetime.datetime.utcnow().strftime('%d_%m_%Y%H:%M:%S:')
    cv2.putText(image, 'Group: ii-18', (10, 90), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 1)

    cv2.imshow('Video', image)

cap.release()
cv2.destroyAllWindows()
























