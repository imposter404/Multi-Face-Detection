import cv2 
import face_recognition
import matplotlib.pyplot as plt 
from PIL import Image

def Face_Detect():
    # load image--------------------------
    global imagePath

    # read iamge--------------------------
    img = cv2.imread(imagePath)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # seclect the model --------------------------------
    face_classifier = cv2.CascadeClassifier( 
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )

    # detect face------------------------------
    ## scale scaleFactor=1.1 = 10% of actual image  

    x=(round(img.shape[0]*0.06))
    face = face_classifier.detectMultiScale( 
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(x,x))

    # Draw box around face----------------------------
    for (x, y, w, h) in face: 
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    # show for Jupyter Notebook ----------------------
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20,10)) 
    plt.imshow(img_rgb) 
    plt.axis('off')

    # show for Python ----------------------
    pil_image=Image.fromarray(img_rgb)
    pil_image.show()




def Face_Extract():
    global imagePath
    image=face_recognition.load_image_file(imagePath)
    face_locations=face_recognition.face_locations(image)
    for face_location in face_locations:
        top,right,bottom,left=face_location
        face_image=image[top:bottom,left:right]


        # show for Jupyter Notebook ----------------------
        pil_image=Image.fromarray(face_image)
        pil_image.show()

        # show for Python ----------------------
        plt.figure()
        plt.imshow(pil_image) 
        plt.axis('off')

imagePath='pic/l1.JPEG'
Face_Detect()
Face_Extract()