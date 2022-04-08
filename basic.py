import cv2 as cv

img = cv.imread('Photos/kevin.jpg')
cv.imshow('Image', img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscaled image', gray)

#Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('BLUR', blur)

#Edge  Cascade
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3) , iterations = 1)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated,(3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize
resized =cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resize)
cv.waitKey(0)