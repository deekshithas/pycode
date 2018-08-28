import cv2
#scaling,resizing and interpolation
img=cv2.imread("flower.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)
img_scaled=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow("scaling linear interpolation",img_scaled)
cv2.waitKey()
#lets double the size of our image
img_scaled1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("scaling-cubic interpolation",img_scaled1)
cv2.waitKey()
#lets skew the resized by setting exact dimensions
img_scaled2=cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow("scaling-skewed size",img_scaled2)
cv2.waitKey()
cv2.destroyAllWindows()

