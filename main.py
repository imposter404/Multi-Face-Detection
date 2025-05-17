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