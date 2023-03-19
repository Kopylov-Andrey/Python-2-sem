import cv2

img = cv2.imread('variant-7.jpg')
img = cv2.flip(img, 0)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Result', img)

cv2.waitKey(0)