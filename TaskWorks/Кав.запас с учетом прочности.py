import matplotlib.pyplot as plt
import numpy as np
import math as mt

d_hk_rec = [2.205, 2.79, 3.435, 4.125, 4.89, 5.715, 6.615, 6.591, 7.5, 8.502, 9.57, 10.7, 11.96, 10.2, 11.31, 12.48]
d_hk = [1.47, 1.86, 2.29, 2.75, 3.26, 3.81, 4.41, 5.07, 5.77, 6.54, 7.36, 8.25, 9.2, 10.2, 11.31, 12.48]
Q_ = [400, 480, 560, 640, 720, 800, 880, 960, 1040, 1120, 1200, 1280, 1360, 1440, 1520, 1600]

f = []
f1 = []
f2 = []

for i in range(0, 16):
        f.append(d_hk[i] + (5*d_hk[i]/d_hk[0])*(mt.exp(-3.5*Q_[i]/(Q_[-1] - Q_[0]))))
        f1.append(d_hk[i])
        #f2.append((mt.exp(-3.5*Q_[i]/(Q_[-1] - Q_[0]))))

plt.plot(Q_, f)
plt.plot(Q_, f1)
print(f)
#plt.plot(Q_, f2)
