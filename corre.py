import cv2
import numpy as np


def detect_object_feature_matching(template_path, input_image_path):
    # Load images (template in grayscale, main image in color)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(input_image_path)

    if template is None or img is None:
        print("Error: Check your file paths. Make sure extensions match precisely.")
        return

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Initialize ORB feature detector
    orb = cv2.ORB_create(nfeatures=2000)

    # Find keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(gray_img, None)

    if des1 is None or des2 is None:
        print("Error: Could not find distinct features in one of the images.")
        return

    # Use Brute-Force Matcher with Hamming distance
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # Sort matches by distance (best matches first)
    matches = sorted(matches, key=lambda x: x.distance)

    # We need a minimum number of good matches to reliably outline the object
    min_match_count = 10
    if len(matches) >= min_match_count:
        # Extract coordinates of matched keypoints
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches[:min_match_count]]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches[:min_match_count]]).reshape(-1, 1, 2)

        # Find the structural alignment using RANSAC to ignore outlier mismatches
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        if M is not None:
            # Get corners of your template image
            h, w = template.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

            # Map the template corners precisely onto the main input image
            dst = cv2.perspectiveTransform(pts, M)

            # Draw a clean, tightly fitting bounding box around the targeted animal
            img = cv2.polylines(img, [np.int32(dst)], True, (0, 255, 255), 3, cv2.LINE_AA)
            print(f"Success! Animal detected using {len(matches[:min_match_count])} unique feature matches.")
        else:
            print("Could not compute valid geometric layout for the matches.")
    else:
        print(f"Not enough clean matches found - {len(matches)}/{min_match_count}")

    # Display the final output
    cv2.imshow('Feature-Based Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Paths updated to point exactly to i1.jpeg
template_path = r"c:\Users\HOME\Downloads\i1.jpeg"
input_image_path = r"c:\Users\HOME\Downloads\Animals.jpg"

# Execute the feature-based detection code
detect_object_feature_matching(template_path, input_image_path)
