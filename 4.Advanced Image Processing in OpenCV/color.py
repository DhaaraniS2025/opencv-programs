import cv2
img = cv2.imread(r"C:\Users\Dhaarani S\Pictures\cats\silver-tabby-cat-sitting-on-green-background-free-photo.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
