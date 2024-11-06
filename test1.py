import skimage.io as io
b = io.imread('backyard.png')
io.imshow(b)
print(b.shape)

print(b[101,202 , :])
print(b[101,202 , 1])
print(b[101,202 , 0:2])
print(b[101,202 , 2:3])