import cv2

img=cv2.imread('abc.jpg')

img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image',img_HSV)

cv2.imshow("Hue",img_HSV[:,:,0])
cv2.imshow("saturation",img_HSV[:,:,1])
cv2.imshow("Value Channel",img_HSV[:,:,2])

cv2.waitKey(0)

cv2.destroyAllWindows()
