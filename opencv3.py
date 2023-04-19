import cv2

#使用する画像の読み込み
img_1 = cv2.imread('sabuntest1.jpg',0)
img_2 = cv2.imread('sabuntest2.jpg',0)

#img_2が300×300だったのでimg_1にサイズを合わせる
img_2_resize = cv2.resize(img_2, (600,600))
cv2.imwrite('sabuntest1.jpg',img_1)
#画像の比較
img_diff = cv2.absdiff(img_1, img_2_resize)
cv2.imshow('sabun-result.jpg',img_diff)
cv2.waitKey(0)