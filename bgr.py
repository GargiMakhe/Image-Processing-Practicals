import numpy as np
import cv2

# Read the image
image = cv2.imread(r"c:\Users\HOME\Downloads\Animals.jpg")

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or unable to load")
else:
    # Split the image into B, G, R channels
    B, G, R = cv2.split(image)

    # Create an array of zeros with the same shape as a single channel
    zeros = np.zeros(image.shape[:2], dtype="uint8")

    # Show the original image
    cv2.imshow('Original', image)
    cv2.waitKey(0)

    # Show blue channel (Merged back into a 3-channel BGR image)
    cv2.imshow('Blue Channel Only', cv2.merge([B, zeros, zeros]))
    cv2.waitKey(0)

    # Show green channel (Merged back into a 3-channel BGR image)
    cv2.imshow('Green Channel Only', cv2.merge([zeros, G, zeros]))
    cv2.waitKey(0)

    # Show red channel (Merged back into a 3-channel BGR image)
    cv2.imshow('Red Channel Only', cv2.merge([zeros, zeros, R]))
    cv2.waitKey(0)

    cv2.destroyAllWindows()
