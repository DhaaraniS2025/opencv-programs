import cv2
import numpy as np

# Load two images
image1 = cv2.imread(r"C:\Users\Dhaarani S\Pictures\honda cars\download (5).jpeg")
image2 = cv2.imread(r"C:\Users\Dhaarani S\Pictures\honda cars\download (4).jpeg")


# Check if images were loaded successfully
if image1 is None or image2 is None:
    print("Error loading images.")
    exit()

# Resize the images to the same dimensions (optional)
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Perform bitwise XOR operation
result = cv2.bitwise_xor(image1, image2)

# Display the original images and the result
cv2.imshow('Bitwise XOR Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()