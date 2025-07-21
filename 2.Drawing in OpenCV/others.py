import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0005.jpg")

ellipse_center = (200, 150)
ellipse_axes = (100, 50)
cv2.ellipse(image, ellipse_center, ellipse_axes, angle=45, startAngle=0, endAngle=360, color=(0, 0, 255), thickness=2)

points = np.array([[300, 50], [400, 150], [450, 100], [350, 30]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

polygon_points = np.array([[100, 300], [200, 300], [150, 400]], np.int32)
polygon_points = polygon_points.reshape((-1, 1, 2))
cv2.fillPoly(image, [polygon_points], color=(255, 0, 0))

start_point = (200,200)
end_point = (300,300)
cv2.arrowedLine(image, start_point, end_point, color=(0, 0, 0), thickness=2)

cv2.imshow('Drawings', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
