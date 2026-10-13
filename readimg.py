import cv2

# 1. Read the image using a raw string for the path
path = r"c:\Users\HOME\Downloads\Medium flowers.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)

# 2. Check if the image was successfully loaded
if img is None:
    print("Error: Could not load image. Check the file path.")
else:
    # 3. Display the image (using a simple window name to avoid escape character errors)
    cv2.imshow("Loaded Image", img)

    # 4. Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
