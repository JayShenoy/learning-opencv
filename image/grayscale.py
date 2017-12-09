import numpy as np
import cv2

img = cv2.imread('me.png', 0)
cv2.imwrite('megray.png', img)