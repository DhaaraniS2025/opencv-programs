import cv2
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\cats\silver-tabby-cat-sitting-on-green-background-free-photo.jpg")
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
