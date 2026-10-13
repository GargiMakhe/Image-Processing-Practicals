# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")

# OpenCV reads in BGR, convert to RGB for correct colors in matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_rgb)

# Remove noise using a median filter
filtered_image = cv2.medianBlur(image, 11)

# Save the filtered image (using correct BGR format for imwrite)
cv2.imwrite("Median_Blur.jpg", filtered_image)

# Convert the filtered image to RGB for plotting
filtered_image_rgb = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

# Plot the blurred image
plt.subplot(1, 2, 2)
plt.title("Median Blur")
plt.imshow(filtered_image_rgb)

plt.tight_layout()
plt.show()
