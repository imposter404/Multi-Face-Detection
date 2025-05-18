# Description
Detecting and Extracting Multiple Faces from a picture using OpenCV and Face Recognition module written in Python


<div align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="50px" alt="Python" />  

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg" height="50px" alt="OpenCV" />
          
       
</div>


# Setup

## Python Dependency 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pypi/pypi-original.svg" height="50px" alt="pypi" />
          


> ``` console
> pip install opencv-python
> pip install face-recognition
> pip install matplotlib
> pip install pillow
> ```

## Dependency Error
you may face this error

```
RuntimeError: Unsuported image type, must be 8bit gray or RGB
```
this error is due to `numpy`,
uninstall `numpy`>=2 and reinstall it

> ``` console 
> pip uninstall numpy
> pip install numpy==1.26.4 
>


---

# Code
> ``` python
> import cv2
> import face_recognition
> import matplotlib.pyplot as plt
> from PIL import Image
> ```

Change your image path
> ``` python 
> imagePath='Data/l1.JPEG'
> ```

Detect Face
> ``` python 
> Face_Detect()
> ```

Extract Face
> ``` python 
> Face_Extract()
> ```


## Run
``` python 
Main.py
```


---
# Disclamer
picture is from `Linus Tech Tips` <br>
[Linus Tech Tips](http://www.youtube.com/@LinusTechTips)
+ add
- delete 
