import cv2

img = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0005.jpg")
gaussian_blur = cv2.GaussianBlur(img, (9, 9), 0)

cv2.imshow("Gaussian Blurred Image", gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
