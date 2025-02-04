import cv2
img1=cv2.imread("C:\\Users\\reshma_koduri\\Downloads\\73-735686_best-ideas-about-elephant-wallpaper-on-pinterest-elephant.jpg")
e1=cv2.getTickCount()
print(e1)
for i in range(5,10,2):
    img1=cv2.medianBlur(img1,i)
e2=cv2.getTickCount()
print(e2)
t=(e2-e1)/cv2.getTickFrequency()
print(t)
cv2.imwrite("./blured.png",img1)#blured file
cv2.imshow('dst',img1)
cv2.waitKey(50000)