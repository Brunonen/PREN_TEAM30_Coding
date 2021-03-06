import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        if cv2.waitKey(2) & 0xFF == ord('w'):
            test = cv2.VideoWriter('capture.divx', 'DIVX', 20.0, (640, 480))
            cv2.VideoWriter.write(test)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
