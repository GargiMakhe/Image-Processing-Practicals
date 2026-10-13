import cv2

# Read the image using a raw string to handle backslashes correctly
image = cv2.imread(r"c:\Users\HOME\Downloads\Animals.jpg")

# Check if image was loaded successfully
if image is None:
    print("Error: Image not found or failed to load. Please check the file path.")
    exit()

# Convert the image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Display the LAB image
cv2.imshow('LAB Image', lab_image)

# Wait for any key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
