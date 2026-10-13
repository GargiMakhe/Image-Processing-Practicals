import cv2
import numpy as np
from matplotlib import pyplot as plt

# --- Load grayscale image ---
# Using raw string (r"...") is correct for Windows paths
img = cv2.imread(r"c:\Users\HOME\Downloads\Animals.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not found. Please check the path and filename.")

# --- Prewitt Edge Detection ---
# Prewitt kernels
kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

# cv2.CV_64F prevents data truncation during gradient subtraction
prewittx = cv2.filter2D(img, cv2.CV_64F, kernelx)
prewitty = cv2.filter2D(img, cv2.CV_64F, kernely)

# Compute magnitude
prewitt_edges = cv2.magnitude(prewittx, prewitty)

# Clip values to 0-255 to prevent overflow wrapping before converting to uint8
prewitt_edges = np.uint8(np.clip(prewitt_edges, 0, 255))

# --- Display Results ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')  # Fixed: Added single quotes around 'gray'
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(prewitt_edges, cmap='gray')  # Fixed: Added single quotes around 'gray'
plt.title('Prewitt Edges')
plt.axis('off')

plt.tight_layout()
plt.show()

# --- Save Result ---
cv2.imwrite('prewitt_edges.jpg', prewitt_edges)
