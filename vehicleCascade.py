#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:18:02 2018

@author: sarahriseden
"""
#code to open the webcam and use the car haarcascade to recognize cars
import cv2

#the xml file that is trained to recognize cars
file = 'cars.xml'
#opening the webcam
cam = cv2.VideoCapture(0)

carCascade = cv2.CascadeClassifier(file)

while True:
    ret, img = cam.read()
    if (type(img) == type(None)):
        break
    
    #converting the image to gray so the computer can 
    #process the colors and images better
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = carCascade.detectMultiScale(gray, 1.1, 1)

    #drawing rectangles onto the video
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    #displaying the video
    cv2.imshow('video', img)
    #press esc 
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()