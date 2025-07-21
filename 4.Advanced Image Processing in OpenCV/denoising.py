import cv2
image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\images (1).jpeg")
denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
cv2.imshow("Denoised", denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()
