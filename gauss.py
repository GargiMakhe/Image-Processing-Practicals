import cv2
import numpy
# using imread()
img = cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")
dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('image', numpy.hstack((img, dst)))

cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)