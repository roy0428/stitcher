import os
import sys
import cv2
from stitchimg import stitchimg

#imgPath = 'D:/research/images216/images216-1'
imgPath = 'D:/research/images216/images216-1-2'
imgList = os.listdir(imgPath)
imgs = []
for imgName in imgList:
    pathImg = os.path.join(imgPath, imgName)
    img = cv2.imread(pathImg)
    img = cv2.resize(img,(1500,1000))
    if img is None:
       print("圖片不能讀取：" + imgName)
       sys.exit(-1)
    imgs.append(img)
#%%
for i in range(1,len(imgs)):
    if i == 1:
        stitchimg(imgs[0],imgs[1], i)
        print('%d sucess' % i)
    elif i >= 2:
        result = cv2.imread('D:/research/result-%d' % (i-1) + '.jpg')
        stitchimg(result,imgs[i], i)
        print('%d sucess' % i)
    