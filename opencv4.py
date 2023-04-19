import cv2
import numpy as np
from matplotlib import pyplot as plt

#元の画像の読み込み
img = cv2.imread("cat.jpg")
img2 = cv2.imread("chihuahua.jpeg")

#shift
shift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptors = shift.detectAndCompute(img, None)
img_sift = cv2.drawKeypoints(img, keypoints, None, flags=4)

shift2 = cv2.xfeatures2d.SIFT_create()
keypoints2, descriptors2 = shift2.detectAndCompute(img2, None)
img_sift2 = cv2.drawKeypoints(img2, keypoints2, None, flags=4)

cv2.imshow("shift", img_sift)
cv2.imwrite("shift.jpg", img_sift)
cv2.imshow("shift2", img_sift2)
cv2.imwrite("shift2.jpg", img_sift2)

#ヒストグラム
#色の指定
colors = ('b','g','r')
  
#ヒストグラムの計算と描画
for i,color in enumerate(colors):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = color)
plt.title("Histgram")
plt.xlabel("Number of pixels")
plt.ylabel("Intensity")
plt.savefig("cat.pdf", format="pdf")
plt.show()

#ヒストグラムの計算と描画
for i,color in enumerate(colors):
    hist2 = cv2.calcHist([img2],[i],None,[256],[0,256])
    plt.plot(hist2,color = color)
plt.title("chihuahua")
plt.xlabel("Number of pixels")
plt.ylabel("Intensity")
plt.savefig("chihuahua.pdf", format="pdf")
plt.show()


cv2.waitKey(0)

