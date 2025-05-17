import cv2 
import matplotlib.pyplot as plt 
import PIL

imagePath=""

def Face_Detect():
    # load image--------------------------
    global imagePath

    # read iamge--------------------------
    img = cv2.imread(imagePath)
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # seclect the model --------------------------------
    face_classifier = cv2.CascadeClassifier( 
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )

    # detect face------------------------------
    ## scale scaleFactor=1.1 = 10% of actual image  

    x=(round(img.shape[0]*0.1))
    face = face_classifier.detectMultiScale( 
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(x,x))