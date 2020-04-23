import cv2
img = cv2.imread('images/ma_photo.jpeg')
img2 = cv2.medianBlur(img,5)
cv2.imshow('ma_photo',img)
cv2.waitKey(0)
cv2.imshow('ma_photo',img2)
cv2.waitKey(0)
