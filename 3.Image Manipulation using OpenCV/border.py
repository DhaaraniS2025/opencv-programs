import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\honda cars\download (4).jpeg")

border_constant = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255, 0, 0])
cv2.imshow("Constant Border", border_constant)
cv2.waitKey(0)
cv2.destroyAllWindows()
