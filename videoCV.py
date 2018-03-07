#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:55:10 2018

@author: sarahriseden
"""

#code to open the webcam and save whatever the camera sees as a video in mp4v format
import cv2
import numpy as np
import matplotlib as mplt

#0 tells the computer to open the first webcam it sees
cam = cv2.VideoCapture(0)

#codec of the video
#mp4v for mac compatibilty
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#object to save the video
out = cv2.VideoWriter('output.m4v', fourcc, 30.0, (640,480))


#infinite loop
while True:
        (grabbed, frame) = cam.read()  # grab the current frame
        frame = cv2.resize(frame, (640,480)) #resizing the frame
        cv2.imshow("Frame", frame)  # display the frame to our screen
        key = cv2.waitKey(33) & 0xFF  # wait until escape is pressed
        out.write(frame)  # Write the video to the file system
        if key==27: #press escape
            break; #stop recording

#closing the camera and display window
cam.release()
out.release()
cv2.destroyAllWindows()