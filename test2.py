import numpy as np

a = np.array([[0,80] , [160,240]])
b = a.astype(np.uint8)

print((a - 20)* 2)
print()
print((b - 20)* 2)
print()
IM = np.array([[0,0,100,100] , [0,0,100,100] , [150,150,250,250] , [150,150,250,250]])

D = np.uint8(np.array([[0,128] , [192,64]]))
r = np.tile(D , (2,2))
IM2 = (IM > r).astype(np.uint8)

print(IM2)