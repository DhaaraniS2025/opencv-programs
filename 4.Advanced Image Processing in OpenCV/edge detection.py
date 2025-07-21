import cv2

# Load an image in grayscale
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0005.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

# Display the original and edge-detected images
cv2.imshow('Edge Detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()