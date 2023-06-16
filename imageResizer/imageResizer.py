import cv2

#config
source = "imageResizer\\john.jpg"
new_image="imageResizer\\new_image.png"
scale_percent=50

image= cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)

#percentagen= of height and width
width = int(image.shape[1]*scale_percent/100)
height = int(image.shape[0]*scale_percent/100)

dsize =(width,height)
#resized image
output = cv2.resize(image,dsize)

cv2.imwrite(new_image,output)
cv2.waitKey(0)