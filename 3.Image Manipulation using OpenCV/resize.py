import cv2

img = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0016.jpg")

resized_img = cv2.resize(img, (300, 200))  # Resize to 300x200

cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
