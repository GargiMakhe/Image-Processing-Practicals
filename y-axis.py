import cv2 as cv
import numpy as np

# 1. Read the image first
img = cv.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg", 0)

# 2. Get the dimensions of the image
rows, cols = img.shape

# 3. Define the transformation matrix (Vertical Shear)
M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])

# 4. Apply the perspective warp using the correct dimensions
sheared_img = cv.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

# 5. Display the result
cv.imshow("Sheared Image", sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()
