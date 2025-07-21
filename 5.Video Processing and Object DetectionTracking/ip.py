import cv2

# Replace the URL with the one shown in your IP Webcam app
url = "http://192.168.0.101:8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Mobile Camera Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
