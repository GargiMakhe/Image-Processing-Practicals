import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the image
# (Ensure this file path exists on your local system)
image_path = r"c:\Users\HOME\Downloads\Medium flowers.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}. Check the path!")
else:
    # 2. Convert BGR (OpenCV default) to RGB (Matplotlib default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 3. Calculate the Laplacian edges (using 64-bit float to catch negative gradients)
    laplacian_gradients = cv2.Laplacian(image, cv2.CV_64F)

    # 4. Sharpen by subtracting the Laplacian from the original image
    # (Converting back to unsigned 8-bit integers and clipping values between 0-255)
    sharpened_image = np.clip(image - laplacian_gradients, 0, 255).astype(np.uint8)
    sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

    # 5. Save the sharpened image back to your drive (OpenCV uses BGR for saving)
    cv2.imwrite("Laplacian_sharpened_image.jpg", sharpened_image)

    # 6. Plot the original vs sharpened image side-by-side
    plt.figure(figsize=(10, 5))

    # Original Plot
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image_rgb)
    plt.axis("off")

    # Sharpened Plot
    plt.subplot(1, 2, 2)
    plt.title("Laplacian Sharpening")
    plt.imshow(sharpened_image_rgb)
    plt.axis("off")

    plt.tight_layout()
    plt.show()
