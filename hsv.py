# Python program to read image
# as HSV color space
# Importing cv2 module
import cv2
# Reads the image
img = cv2.imread(r"c:\Users\HOME\Downloads\Animals.jpg")
# Converts to HSV color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Shows the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()