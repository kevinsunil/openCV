import cv2 as cv
import numpy as np

blank = np.zeroes((500,500,3), dtype= 'uint8')
#1 paint the  whole image

blank[:]= 0,255,0
cv.imshow('Green', blank)
#2 paint a certain section

blank[200:300, 300:400]= 0,255,0
cv.imshow('Green Square', blank)

#3 draw a rectangle
cv.rectangle(blank,(0,0),(250,220),(0,255,0),thickness = 2)
cv.imshow('Green  Rectangle', blank)

#4 Filled rectangle
cv.rectangle(blank,(0,0),(250,270),(0,255,0),thickness = cv.Filled)
cv.imshow('Green Filled Rectangle', blank)

#5 draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

#5 filled circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

#6 draw  a line
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Line', blank)

#7 add a text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('TEXT', blank)

cv.waitKey(0)