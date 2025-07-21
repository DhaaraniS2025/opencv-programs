import cv2

image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0010.jpg")
cv2.circle(image, (250, 250), 50, (0, 0, 255), 2)
cv2.imshow('Circle Example', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
