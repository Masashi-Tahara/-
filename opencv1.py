import numpy as np

arr1 = np.array([[1,2], [3, 4]])
arr2 = np.array([[10, 20], [30, 40]])

#足し算
arr3 = arr1 + arr2
#引き算
arr4 = arr2 - arr1
#掛け算
arr5 = arr1 * arr2
#割り算
arr6 = arr1 / arr2

#計算結果の表示
print("add")
print(arr3)
print("sub")
print(arr4)
print("mal")
print(arr5)
print("dev")
print(arr6)

