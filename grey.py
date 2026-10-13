import os
import cv2

# Use a raw string (r"...") to safely handle Windows backslashes
file_path = r"c:\Users\HOME\Downloads\Animals.jpg"

# 1. Double-check if the file actually exists at that path
if not os.path.exists(file_path):
    print(f"Error: The file path does not exist. Please check for typos: {file_path}")
else:
    # 2. Read image directly in grayscale mode
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # 3. Check if OpenCV successfully decoded the image
    if img is None:
        print("Error: Image found, but OpenCV could not decode it. (Is the file corrupted or an unsupported format?)")
    else:
        # 4. Show the grayscale image
        cv2.imshow('Grayscale Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
