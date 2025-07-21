import cv2

# Load an image
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\spring-wallpaper-creating-award-winning-photograph-pic-encapsulates-timeless-beauty-tranquility-nature-351383535.webp")

# Apply average blur
blurred_image = cv2.blur(image,(3,3))

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
