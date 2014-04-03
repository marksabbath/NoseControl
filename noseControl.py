#/usr/bin/python

import numpy as np
import cv2
from pymouse import PyMouse

m = PyMouse()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')


capture = cv2.VideoCapture()
capture.open(-1)
while True:
   img = capture.read()[1]
   img = np.asarray(img[:,:])
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   nose = nose_cascade.detectMultiScale(gray, 1.3, 5)
   for (x,y,w,h) in nose:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      fat_conv = 2.5
      m.move(x*fat_conv,y*fat_conv)
      print 'x:', x * fat_conv, 'y: ', y * fat_conv

   cv2.imshow('img',img)
   if cv2.waitKey(10) == 27:
      break

cv2.destroyAllWindows()
