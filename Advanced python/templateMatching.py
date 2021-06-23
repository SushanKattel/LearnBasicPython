import cv2
import numpy as np

img_rgb = cv2.imread('C:/Users/asus/Desktop/yantraDataset/mainsample.jpg',0)
w1, h1 = img_rgb.shape[::-1]
w1 = int(w1*0.5)
h1 = int(h1*0.5)
img_gray = cv2.resize(img_rgb,(w1,h1))

template = cv2.imread('C:/Users/asus/Desktop/yantraDataset/test_template.jpg',0)
#template = cv2.imread('C:/Users/asus/Desktop/yantraDataset/template.png',cv2.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]
w = int(w*0.5)
h = int(h*0.5)
template = cv2.resize(template,(w,h))



res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
loc = np.where(res > 0.8)



for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

cv2.imshow('image',img_rgb)
# cv2.imshow('result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()