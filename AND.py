import cv2
import numpy as np

# Load the images
img1 = cv2.imread(r"c:\Users\HOME\Downloads\opensky.jpg")
img2 = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")

# Check if images loaded successfully
if img1 is None or img2 is None:
    print("Error: One or both images could not be loaded. Check your file paths.")
else:
    # Resize img2 to match the dimensions of img1 to prevent size mismatch errors
    height, width, channels = img1.shape
    img2_resized = cv2.resize(img2, (width, height))

    # Perform the bitwise AND operation
    dest_and = cv2.bitwise_and(img2_resized, img1, mask=None)

    # Display the result
    cv2.imshow('Bitwise And', dest_and)

    # De-allocate memory when 'ESC' (27) or any key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
