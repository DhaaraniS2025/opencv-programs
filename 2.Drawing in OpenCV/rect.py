import cv2
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0006.jpg")
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 255), 4)
cv2.imshow('Rectangle Example', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
