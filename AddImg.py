import cv2
import numpy as np

# Load the images
image1 = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")
image2 = cv2.imread(r"c:\Users\HOME\Downloads\opensky.jpg")

# Ensure images are loaded successfully before blending
if image1 is None or image2 is None:
    print("Error: One or both images could not be loaded. Check your file paths.")
else:
    # Resize image2 to match image1 dimensions if they are not the same size
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Perform weighted addition
    weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

    # Display the result with a corrected string argument
    cv2.imshow("Weighted Image", weightedSum)

    # Wait for the ESC key (27) to close the window
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()
