import cv2
import dropbox
import time
import random

startTime=time.time()

def takeSnapshot():
    number=random.randint(1,100)
    
    videoCaptureObject=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accessToken="IupQZpjYg6cAAAAAAAAAAXvFrykkADAIvVur-uNh2Zv2Tme3VLjAyYUXR-6oYoAM"
    file=imageName
    fileFrom=file
    fileTo="/Project102/"+(imageName)
    dbx=dropbox.Dropbox(accessToken)

    with open(fileFrom,'rb')as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=takeSnapshot()
            uploadFile(name)
main()