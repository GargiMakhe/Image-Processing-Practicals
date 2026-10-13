import cv2
import numpy as np

# Load the input image in BGR format
image1 = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")

# Convert the input image to grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Apply different simple thresholding techniques (Threshold value = 120, Max value = 255)
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# Display the thresholded output images
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# Wait until any key is pressed.
# If the 'ESC' key (ASCII 27) is pressed, close the windows.
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
