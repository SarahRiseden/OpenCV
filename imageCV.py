#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:00:07 2018

@author: sarahriseden
"""
#code to read in an image, conver it to grayscale, draw shapes, and move pieces of the image
import cv2
import numpy as np
import matplotlib.pyplot as plt



#image = still frame
#video = frames per second

#reading in the image
img = cv2.imread("sarah.jpg", cv2.IMREAD_GRAYSCALE) #replace filename.jpg with any file name for any image
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1


#drawing a rectangle around my face and then moving it to the topleft corner
#parameters(img, topleft(x1,y1), bottomright(x2,y2), color(b,g,r), line witdh)
cv2.rectangle(img, (350,250), (550,450), (0,0,0), 5)
#img[y1:y2, x1:x2]
myFace = img[250:450, 350:550]
img[0:200, 0:200] = myFace


cv2.imshow("image", img) #first parameter is the name of the display window
#waits until any key is pressed to close the image
cv2.waitKey(0)
cv2.destroyAllWindows()

#saving the new image to the project directory
cv2.imwrite("sarah.png", img) #".png" is the name of the new image





