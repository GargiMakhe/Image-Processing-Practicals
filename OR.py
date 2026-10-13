import cv2
import numpy as np

# Load the two images
# Note: For bitwise operations, img1 and img2 must be the exact same size (width and height)
img1 = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")
img2 = cv2.imread(r"c:\Users\HOME\Downloads\opensky.jpg")

# Perform bitwise OR operation
dest_or = cv2.bitwise_or(img2, img1, mask=None)

# Display the output window (added missing quotes around 'Bitwise OR')
cv2.imshow('Bitwise OR', dest_or)

# De-allocate any associated memory usage when Esc key (27) is pressed
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
