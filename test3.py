import skimage.io as io 
import matplotlib.pyplot as plt
import numpy as np
import skimage.exposure as ex

x = np.uint8(range(256))
y_a = x - 100
xf = np.float64(x)
y_bf = np.uint8(np.clip(xf - 128 , 0, 255))
plt.figure() , plt.plot(x,y_a , x , y_bf)
plt.legend(['y_a' , 'y_bf'])

hm = io.imread('handmade.png')
hm_g1 = ex.adjust_gamma(hm, 5)
hm_g2 = ex.adjust_gamma(hm, 10)
hm_h = ex.equalize_hist(hm)
# 改成 plt.show() 來確保圖像顯示不會自動關閉
f = plt.figure()
plt.hist(hm_h.flatten(), bins=256)
plt.show()
