import matplotlib.pyplot as plt #importing matplotlib
import cv2 # importing required libraries of opencv

#reads image data
img = plt.imshow('image1.png')

#calculating histogram
plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# load an image in grayscale mode
img = cv2.imread('image1.png',0)


# calculate frequency of pixels in range 0-255
histg = cv2.calcHist([img],[0],None,[256],[0,256])

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('ex.jpg',0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()

