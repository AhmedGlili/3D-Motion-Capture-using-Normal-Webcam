import cv2
import time
import PoseModule as pm
cap = cv2.VideoCapture('Video.mp4')
detector = pm.PoseDetector()
lmString=''
posList=[]
while True:
    success, img = cap.read()
    img=detector.findPose(img)
    lmList,bboxInfo=detector.findPosition(img)
    if bboxInfo:
        lmString=''
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
    posList.append(lmString)
    print(len(posList))
    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFrikhaFile.txt",'w')as f:
            f.writelines(["%s\n" % item for item in posList])

