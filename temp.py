import cv2 
from matplotlib import pyplot as plt 
img = cv2.imread('C:\\Pictures\\image2.png',0) 

# alternative way to find histogram of an image 
plt.hist(img.ravel(),256,[0,256]) 
plt.show() 


