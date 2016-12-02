import numpy
import numpy as np
import cv2
from RomanCharacterPicture import RomanCharacterPicture
import time

cap = cv2.VideoCapture(1)
hasCharacterBeenEvaluated = False
RomanPictures = []
CharacterEval = [0]*100

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not hasCharacterBeenEvaluated:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV

        # lower mask (0-10)
        lower_red = np.array([0, 100, 10])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170, 100, 100])
        upper_red = np.array([179, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        # Combine Masks
        mask = mask0 + mask1
        red_hue_image = cv2.addWeighted(mask0, 1.0, mask1, 1.0, 0.0)
        test = cv2.GaussianBlur(red_hue_image, (9,9), 0)

        # Get Contours
        contours, hierarchy = cv2.findContours(test, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        barCount = 0

        # cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
        rectangleList = []

        # Loop Through Found contours
        for foundRectangle in contours:
            if barCount <= 2:
                approxDistance = cv2.arcLength(foundRectangle,True) * 0.02

                approxCurve = cv2.approxPolyDP(foundRectangle, approxDistance, True)

                # Only look for rectangles
                if len(approxCurve) == 4:
                    rect = cv2.boundingRect(approxCurve)
                    # Only save Rectangles with height of 250+
                    if rect[3] >= 300:
                        rectangleList.append(rect)
                        barCount += 1

        # Only if exactly 2 Red bars were found, save them to the Picture array
        if barCount == 2:
            RomanPictures.append(RomanCharacterPicture(frame, rectangleList))

        if len(RomanPictures) >= 5:
            for pictures in RomanPictures:
                index = pictures.evaluatePicture()
                print index
                CharacterEval[index] += 1


            maxCharacter = 0
            characterCount = 1
            while characterCount <= 6:
                if maxCharacter < CharacterEval[characterCount]:
                    maxCharacter = characterCount
                characterCount += 1

            if maxCharacter == 6:
                maxCharacter = 4

            print "Roman: " + str(maxCharacter)
            hasCharacterBeenEvaluated = True

        cv2.imshow('frame', frame)
        #time.sleep(0.5)q

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()