import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\gettyimages-829823474-612x612.jpg")
(h, w) = image.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
