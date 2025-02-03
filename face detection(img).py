import cv2

alg="haarcascade_frontalface_default.xml"

#to load the algorithm
haar_cascade=cv2.CascadeClassifier(alg)
video_path="1.mp4"
img=cv2.imread(video_path)


while True:
    #to read the frame
    text="No Face"
    
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)

    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,123),7)
        text="Face Detected"

    print(text)
    cv2.imshow("FaceDetect",img)

    key=cv2.waitKey(10)
    if key==27: #escape key value=27
        break

cam.release()
cv2.destroyAllWindows()
