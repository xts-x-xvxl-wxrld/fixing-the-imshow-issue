import cv2


def videoCap(videoSource=0):
    cap = cv2.VideoCapture(videoSource)
    if not cap.isOpened():
        return False
    else:
        return cap


cap = videoCap()
while cap:
    ret, frame= cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()