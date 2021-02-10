# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:51:38 2021

@author: I340968
"""

# Decoding an message into QRcode

import qrcode
img=qrcode.make("I test QR code") # result in image
img.save("qrcode.jpg")

img1=qrcode.make("https://www.youtube.com/watch?v=QoCAYcZ_Qc8&t=194s")
img1.save("qrcode1.jpg")

#Encoding the QR code

import cv2
d = cv2.QRCodeDetector()
val,point,striaght_qrcode = d.detectAndDecode(cv2.imread("qrcode.jpg"))
print(val)
print(point)
print(striaght_qrcode)