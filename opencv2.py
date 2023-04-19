import cv2

#元の画像の読み込み
img = cv2.imread("cat.jpg")

#倍率を変更した画像
resize = cv2.resize(img, (400, 400))

#回転した画像
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#二値化のためのグレースケールの画像の読み込み
gray = cv2.imread("cat.jpg", 0)

#二値化した画像
ret, img_threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

#それぞれの画像の表示
cv2.imshow("img", img)
cv2.imshow("resize", resize)
cv2.imshow("rot", rot)
cv2.imshow("thre", img_threshold)

cv2.imwrite("original_img.jpg", img)
cv2.imwrite("resize.jpg", resize)
cv2.imwrite("rot.jpg", rot)
cv2.imwrite("thre.jpg", img_threshold)
cv2.waitKey(0)