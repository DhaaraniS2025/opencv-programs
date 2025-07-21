import cv2
img = cv2.imread(r"C:\Users\Dhaarani S\Pictures\spring-wallpaper-creating-award-winning-photograph-pic-encapsulates-timeless-beauty-tranquility-nature-351383535.webp")
resized1 = cv2.resize(img, (300, 200)) 
cv2.imshow("Original", img)
cv2.imshow("Resized by Dimensions", resized1)
cv2.waitKey(0)
cv2.destroyAllWindows()
