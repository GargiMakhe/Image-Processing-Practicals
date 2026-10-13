import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r"c:\Users\HOME\Downloads\Medium flowers.jpg")
plt.imshow(img)
plt.waitforbuttonpress()
plt.close(all)