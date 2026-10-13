import cv2
import numpy as np

# 1. Load the images
image1 = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")
image2 = cv2.imread(r"c:\Users\HOME\Downloads\opensky.jpg")

# 2. Safety Check: Verify that the files were actually found and loaded
if image1 is None or image2 is None:
    print("Error: One or both images could not be loaded. Check your file paths!")
else:
    # 3. Fix Dimension Mismatch: Resize image2 to match image1's size
    height, width, channels = image1.shape
    image2 = cv2.resize(image2, (width, height))

    # 4. Perform subtraction
    sub = cv2.subtract(image1, image2)

    # 5. Display the result
    cv2.imshow('Subtracted Image', sub)

    # De-allocate any associated memory usage safely
    if cv2.waitKey(0) & 0xFF == 27:  # Press 'ESC' to exit
        cv2.destroyAllWindows()
