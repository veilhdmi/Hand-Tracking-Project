import cv2
from playsound import playsound
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5,maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    hands = detector.findHands(img,draw=False)  # with draw
    #hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        totalFingers1 = fingers1.count(1)
        cv2.putText(img, str(handType1)+str(totalFingers1), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 10)


        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)
            totalFingers2 = fingers2.count(1)
            cv2.putText(img, str(handType2)+str(totalFingers2), (45, 100), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 10)
            # Find Distance between two Landmarks. Could be same hand or different hands
            #length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
            if fingers1[1] ==1 and fingers1[4] == 1 and fingers1[0] ==0 and fingers1[2] ==0 and fingers1[3] ==0:
                cv2.putText(img, str("ROCKANDROLL"), (100, 200), cv2.FONT_HERSHEY_PLAIN, 10,
                            (0, 255, 0), 10)
            if fingers1[1] ==1 and fingers1[4] == 1 and fingers1[0] ==1 and fingers1[2] ==0 and fingers1[3] ==0:
                cv2.putText(img, str("spiderman uwu"), (100, 200), cv2.FONT_HERSHEY_PLAIN, 10,
                            (0, 255, 0), 10)
    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()