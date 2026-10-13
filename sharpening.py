import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the image
# Using raw string (r"...") prevents errors from backslashes in Windows paths
image_path = r"c:\Users\HOME\Downloads\Medium flowers.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}. Check the file path.")
else:
    # 2. Convert from BGR to RGB for correct plotting colors in Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 3. Create the sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # 4. Sharpen the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Convert the sharpened image to RGB for plotting
    sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

    # 5. Save the sharpened image
    # Added quotes around the filename and renamed it so you don't overwrite your original file
    output_path = r"c:\Users\HOME\Downloads\Medium_flowers_sharpened.jpg"
    cv2.imwrite(output_path, sharpened_image)
    print(f"Sharpened image successfully saved to: {output_path}")

    # 6. Plot the side-by-side comparison
    plt.figure(figsize=(10, 5))

    # Original Image Plot
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image_rgb)
    plt.axis('off')  # Hides coordinate axes for a cleaner look

    # Sharpened Image Plot
    plt.subplot(1, 2, 2)
    plt.title('Sharpened')
    plt.imshow(sharpened_image_rgb)
    plt.axis('off')

    plt.tight_layout()
    plt.show()
