import cv2

image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\WhatsApp Image 2025-06-22 at 11.05.46_f6204a4b.jpg")

# Apply median blur with a kernel size of 3x3
blurred_image = cv2.medianBlur(image, 9)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()