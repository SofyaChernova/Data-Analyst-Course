import matplotlib.pyplot as plt
import numpy as np

h0 = 1.160017694469840E+01
h1 = -2.1285064766839E-02
h2 = 8.1053829725E-05
h3 = -1.2486931789E-07
h4 = 7.6422662867E-11
h5 = -1.6343040267E-14

h_poly = [1.160017694469840E+01, -2.1285064766839E-02, 8.1053829725E-05, -1.2486931789E-07, 7.6422662867E-11, -1.6343040267E-14]

p0 = 1.8990275694444E+00
p1 = -4.5473567230556E-03
p2 = 1.8102037379734E-05
p3 = -2.5991589902122E-08
p4 = 1.5375803357656E-11
p5 = -3.2234459276425E-15

#p_poly

Q_range = range(0, 3000, 50)

#H = h0 + h1 * Q + h2 * pow(Q, 2) +h3 * pow(Q, 3) + h4 * pow(Q, 4) + h5 * pow(Q, 5)
#P = p0 + p1 * Q + p2 * pow(Q, 2) +p3 * pow(Q, 3) + p4 * pow(Q, 4) + p5 * pow(Q, 5)

H = []
P = []
for Q in Q_range:
    H.append(h0 + h1 * Q + h2 * pow(Q, 2) +h3 * pow(Q, 3) + h4 * pow(Q, 4) + h5 * pow(Q, 5))
    P.append(p0 + p1 * Q + p2 * pow(Q, 2) +p3 * pow(Q, 3) + p4 * pow(Q, 4) + p5 * pow(Q, 5))

#plt.plot(Q_range, H)
plt.plot(Q_range, P)


def polynom(n, x, a):
    k = range(n-2, -1, -1)
    s = a[n-1]
    for i in k:
        s = s * x + a[i]
    return s

print(polynom(6, 2500, h_poly))

