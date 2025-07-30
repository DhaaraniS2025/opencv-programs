import cv2
img = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0008.jpg")
cv2.line(img, (50, 100), (300, 100), (255, 0, 0), 3)
cv2.imshow('Line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
