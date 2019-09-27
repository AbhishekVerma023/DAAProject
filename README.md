# City Population Analysis using OpenCV

The images of buildings are captured and represented in a graph in the form of filled histogram. 
It is required to find out the dense area in city based on maximum area of region covered under the histogram.

### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install OpenCV.

```bash
pip install opencv-python
```


This will install OpenCV on your Anaconda Command prompt and get you up and running

```python
import cv2 
```
Import OpenCV packages


```python
img = cv2.imread('C:\\Pictures\\image1.png',0)
```
Read the image with imread() method


```python
plt.hist(img.ravel(),256,[0,256]) 
plt.show() 
```
Plotting the histogram of the image using pixel densities


## Analyzing the test results
Tones
The region where most of the brightness values are present is called the "tonal range." 
Tonal range can vary drastically from image to image, so developing an intuition for how numbers map to actual brightness values is often critical—both before and after the photo has been taken. 
There is no one "ideal histogram" which all images should try to mimic; histograms should merely be representative of the tonal range in the scene and what the test wishes to convey.
Cotrast
A histogram can also describe the amount of contrast. Contrast is a measure of the difference in brightness between light and dark areas in a scene. 
Broad histograms reflect a scene with significant contrast, whereas narrow histograms reflect less contrast and may appear flat or dull.
Photos taken in the open lands will have low contrast, while those taken under strong daylight and excessive building cover will have higher contrast.

## Built With

* [Anaconda](https://www.anaconda.com/distribution/) - The all in one place for Python
* [Spyder IDE](https://www.spyder-ide.org/) - The Python IDE

## Acknowledgments

* Seaborn
* Cambridge in colour

