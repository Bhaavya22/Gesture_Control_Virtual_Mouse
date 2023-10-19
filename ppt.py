import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Variables
width, height = 1280, 720
folderpath = "ppt"

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Importing images
pathImages = sorted(os.listdir(folderpath), key=len)
print(pathImages)

# Variables
imgnum = 0
hs, ws = int(120 * 1.2), int(213 * 1.2)
gestureThre = 300
buttonPressed = False
buttoncounter = 0
buttondelay = 10

# Hand detector
detect = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    if not success:
        print("Error: Unable to capture frame from the webcam.")
        break

    img = cv2.flip(img, 1)
    pathfullimage = os.path.join(folderpath, pathImages[imgnum])
    imgcurrent = cv2.imread(pathfullimage)

    # Check if the frame is not empty before processing
    if not img.any():
        print("Error: Captured frame is empty.")
        break

    hands, img = detect.findHands(img)
    cv2.line(img, (0, gestureThre), (width, gestureThre), (0, 255, 0), 10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detect.fingersUp(hand)

        cx, cy = hand['center']
        # print(fingers)
        lmlist = hand.get('lmlist', [])
        indexfinger = lmlist[8] if lmlist else (0, 0)

        if cy <= gestureThre:  # if hand is at the height of the face
            # gesture 1 - left
            if fingers == [1, 0, 0, 0, 0]:
                print("left")

                if imgnum > 0:
                    buttonPressed = True
                    imgnum -= 1
            # gesture 2 - right
            if fingers == [0, 0, 0, 0, 1]:
                print("right")

                if imgnum < len(pathImages) - 1:
                    buttonPressed = True
                    imgnum += 1

        # gesture 3 - show pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(img, indexfinger, 12, (0, 0, 255), cv2.FILLED)

    # button pressed iterations
    if buttonPressed:
        buttoncounter += 1
        if buttoncounter > buttondelay:
            buttoncounter = 0
            buttonPressed = False

    # Resizing webcam feed
    imgsmall = cv2.resize(img, (ws, hs))

    # Resize the presentation image to fit within the window without distorting its aspect ratio
    aspect_ratio = imgcurrent.shape[1] / imgcurrent.shape[0]
    new_width = int(min(width, height * aspect_ratio))
    imgcurrent = cv2.resize(imgcurrent, (new_width, int(new_width / aspect_ratio)))

    # Extracting dimensions of the slide image
    h, w, _ = imgcurrent.shape

    # Placing webcam feed in the top right corner
    imgcurrent[0:hs, w - ws:w] = imgsmall

    cv2.imshow("Images", img)
    cv2.imshow("Presentation", imgcurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()