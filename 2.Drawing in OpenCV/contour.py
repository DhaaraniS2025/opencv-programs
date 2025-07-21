import cv2

# Load the image
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0017.jpg")

# Resize the image (e.g., width=800, height=600)
resized_image = cv2.resize(image, (800, 600))  # You can adjust the size as needed

# Convert to grayscale
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours in green
cv2.drawContours(resized_image, contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imshow("Contours", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

