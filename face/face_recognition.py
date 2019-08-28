# Import OpenCV2 for image processing
import cv2
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np

class RaspiCamera:

    def __init__(self, width, height):

        self.camera = PiCamera()
        self.camera.resolution = (width, height)
        #self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=self.camera.resolution)
        self.capture_continuous = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)

    def capture(self):

        frame = self.capture_continuous.next()
        image = self.rawCapture.array
        self.rawCapture.truncate(0)

        return image

if __name__ == "__main__":

    camera = RaspiCamera(640, 480)
    frame1 = camera.capture()
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the trained mode
    recognizer.read('trainer/trainer.yml')

    # Load prebuilt model for Frontal Face
    cascadePath = "haarcascade_frontalface_default.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # Set the font style
    font = cv2.FONT_HERSHEY_SIMPLEX


    while True:
        
        gray=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which ID
            Id = recognizer.predict(gray[y:y+h,x:x+w])

            # Check the ID if exist 
            if(Id == 5):
                Id = "Prakash"
            #If not exist, then it is Unknown
            elif(Id == 2):
                Id = "Jenifer"
            else:
                print(Id)
            #Id = "Unknow"

            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
        
        #cv2.imshow("original",img)
        cv2.imshow("recog",frame1)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv2.destroyAllWindows()

