import cv2 as cv
import numpy as np

# 1. Load the image in grayscale (0)
img = cv.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg", 0)

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not open or find the image. Check the file path.")
else:
    rows, cols = img.shape

    # 2. Define the transformation matrix for horizontal shearing
    M = np.float32([[1, 0.5, 0],
                    [0, 1,   0],
                    [0, 0,   1]])

    # 3. Apply the perspective transformation
    sheared_img = cv.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

    # 4. Display the result using a proper window title
    cv.imshow('Sheared Image', sheared_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
