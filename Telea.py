import cv2

# 1. Read only the damaged image
img_path = r"c:\Users\HOME\Downloads\cat_damaged_img.jpg"
img = cv2.imread(img_path)

if img is None:
    print("Error: Could not load the image. Check the file path.")
else:
    # 2. Automatically generate the mask from the image itself
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # 3. Apply the Telea Inpainting algorithm
    dst = cv2.inpaint(img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # 4. Save the result
    output_path = r"c:\Users\HOME\Downloads\restored_image_telea.jpg"
    cv2.imwrite(output_path, dst)
    print(f"Success! Restored image saved to: {output_path}")

    # 5. Show the image in a popup window
    cv2.imshow('Original Damaged Image', img)
    cv2.imshow('Generated Mask', mask)
    cv2.imshow('Telea Inpainted Result', dst)

    print("Press any key on your keyboard while the image window is active to close it.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()