import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0008.jpg", 0)
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(thresh, kernel, iterations=1)
dilated = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
