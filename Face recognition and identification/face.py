# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:03:56 2018

@author: DELL
"""
# recognize? deep learned model predict keras tensorflow pytorch scikit learn
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pickle
face_cascade=cv2.CascadeClassifier("cascade/data/haarcascade_frontalface_alt2.xml")
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels={}
with open("labels.pickle","rb") as f:
    oglabels=pickle.load(f)
    labels={v:k for k,v in oglabels.items()}
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        
        id_,conf=recognizer.predict(roi_gray)
        
        if conf>60:    # and conf<=85:
            print(id_)
            print(labels[id_])
            font=cv2.FONT_HERSHEY_PLAIN
            name=labels[id_]
            color=(0,0,250)
            storke=2
            cv2.putText(frame,name+" "+str(conf),(x,y),font,1.3,color,storke,cv2.LINE_AA)
        img_item="my_image.png"
        cv2.imwrite(img_item,roi_gray)
        
        #detection draw rectangle
        color=(250,0,0) #BGR 0-255
        stroke=2 # line thickness
        end_cord_x=x+w
        end_cord_y=y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke) 
    cv2.imshow('smile',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

