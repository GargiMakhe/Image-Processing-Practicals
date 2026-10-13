
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found. Check the image path.")
else:
    # Apply Median Filter
    filtered_img = cv2.medianBlur(img, 5)

    # Convert images from BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    filtered_rgb = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)

    # Display original and filtered images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_rgb)
    plt.title("Median Filtered Image")
    plt.axis("off")

    plt.show()
