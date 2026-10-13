import cv2
import numpy as np
from matplotlib import pyplot as plt

# --- Load grayscale image ---
img = cv2.imread(r"c:\Users\HOME\Downloads\Animals.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("Image not found. Please check the path and filename.")

# --- Sobel Edge Detection ---
# Sobel in X and Y directions
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Compute magnitude
sobel_edges = cv2.magnitude(sobelx, sobely)
sobel_edges = np.uint8(sobel_edges)

# --- Display Results ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')  # Fixed: removed quotes from img, added quotes to 'gray'
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edges')
plt.axis('off')

plt.tight_layout()
plt.show()

# --- Save Result (optional) ---
cv2.imwrite('sobel_edges.jpg', sobel_edges)
