import cv2 as cv
import numpy as np

# 1. Load the image in grayscale (0)
image_path = r"c:\Users\HOME\Downloads\Medium flowers.jpg"
img = cv.imread(image_path, 0)

# Check if the image loaded successfully
if img is None:
    print(f"Error: Could not open or find the image at {image_path}")
else:
    # 2. Shrink the image to a fixed size (250 width, 200 height)
    img_shrinked = cv.resize(img, (250, 200), interpolation=cv.INTER_AREA)

    # 3. Enlarge the shrinked image by 1.5x along both axes
    img_enlarged = cv.resize(img_shrinked, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)

    # 4. Display the results in separate windows
    cv.imshow("Shrinked Image", img_shrinked)
    cv.imshow("Enlarged Image", img_enlarged)

    # 5. Wait for a key press and close the windows
    cv.waitKey(0)
    cv.destroyAllWindows()
