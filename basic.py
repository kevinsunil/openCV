import cv2 as cv

img = cv.imread('Photos/kevin.jpg')
cv.imshow('Image', img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscaled image', gray)

#Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('BLUR', blur)

cv.waitKey(0)