import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
# Note: Using a raw string (r"...") prevents escape character issues in Windows paths
image_path = r"c:\Users\HOME\Downloads\Medium flowers.jpg"
image = cv2.imread(image_path)

# Verify if the image was loaded correctly
if image is None:
    raise FileNotFoundError(f"Could not load image at {image_path}. Check the file path.")

# Convert BGR (OpenCV) to RGB (Matplotlib) for correct plotting
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Adjust the brightness and contrast
# Adjusts the brightness by adding 10 to each pixel value
brightness = 10
# Adjusts the contrast by scaling the pixel values by 2.3
contrast = 2.3

# Apply brightness and contrast adjustments
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

# Convert the modified image to RGB for correct plotting
image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

# Save the modified image (Keep it in BGR format for cv2.imwrite)
cv2.imwrite('modified_image.jpg', image2)

# Set up the matplotlib figure size
plt.figure(figsize=(10, 5))

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis('off')  # Hides axis ticks for a cleaner look

# Plot the modified image
plt.subplot(1, 2, 2)
plt.title("Brightness & Contrast")
plt.imshow(image2_rgb)
plt.axis('off')  # Hides axis ticks for a cleaner look

# Display the plots
plt.tight_layout()
plt.show()
