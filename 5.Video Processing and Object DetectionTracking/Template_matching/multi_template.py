import cv2
import numpy as np
img_rgb = cv2.imread(r"C:\Users\Dhaarani S\Downloads\Mainimage.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(r"C:\Users\Dhaarani S\Downloads\template1.jpg",0)
w, h = template.shape[::-1]  #reverses template result(h,w) into (w,h)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold =0.8 #keeps only 80% matches
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]): # (y,x) to (x,y), (y,x) because(row,coloumn)
    cv2.rectangle(img_rgb, pt,(pt[0] + w, pt[1] + h), (0,0,255),2)
cv2.imshow('MultipleObject',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
#loc = np.where(res >= threshold)          loc = (array_of_y_coords, array_of_x_coords)
#loc[::-1]
#Reverses the tuple so you get: (array_of_x_coords, array_of_y_coords)
#*loc[::-1]
#The * operator unpacks the two arrays so that they become two separate arguments to zip():
#zip(array_of_x_coords, array_of_y_coords)
#for pt in zip(...)
#Now, zip() combines the coordinates into (x, y) points:
#[(x1, y1), (x2, y2), (x3, y3), ...]