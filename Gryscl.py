import cv2

# 1. Set the correct path to your image
path = r'c:\Users\HOME\Downloads\Medium flowers.jpg'

# 2. Read the image in grayscale
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if img is not None:
    # 3. Display the image with a clean window title
    cv2.imshow("Grayscale Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load image. Please check the file path.")
