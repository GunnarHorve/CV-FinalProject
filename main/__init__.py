import cv2
from matplotlib import pyplot as plt

mat = cv2.imread('testimage.jpg',cv2.IMREAD_GRAYSCALE)
col = cv2.imread('testimage.jpg')
ret,thresh1 = cv2.threshold(mat,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='Greys')
plt.xticks([]), plt.yticks([])
plt.show()
print("hello world")