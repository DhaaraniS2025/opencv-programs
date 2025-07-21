import cv2
import numpy as np

image1 = cv2.imread(r"C:\Users\Dhaarani S\Pictures\honda cars\download (8).jpeg")
image2 = cv2.imread(r"C:\Users\Dhaarani S\Pictures\honda cars\images.jpeg")
image1 = cv2.resize(image1,(image2.shape[1], image2.shape[0]))
result = cv2.bitwise_or(image1, image2)
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise OR Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()