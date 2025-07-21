import cv2

# Replace with the path to your video file
video_path = r"C:\Users\Dhaarani S\Videos\Nature Video 30 SecondsWhatsApp Status VideoNature Background Videos - Round the Clock (1080p, h264).mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    
    if not ret:
        break  # End of video

    cv2.imshow("Video Playback", frame)

    # Press 'q' to exit early
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
