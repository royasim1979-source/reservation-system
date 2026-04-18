import numpy as np
arr1 = np.array([[1,2,3],[5,0,10],[-1,-9,0]])
arr2 = np.array([[1,0,3],[5,1,-10],[-1,9,-1]])
print(arr1+arr2)
print(np.ndim(arr1))
print(np.std(arr1))
print(arr1[arr1%2==0])
print(np.linalg.det(arr1))