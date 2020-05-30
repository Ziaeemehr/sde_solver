import numpy as np
import matplotlib.pyplot as plt
from numpy import exp
import pylab as pl

num_sims = 5  # Display five runs

T = 1
N = 2**10
dt = T / N
Xzero = 1.0
alpha = 2.0
beta = 1.0
t = np.arange(0, T, dt)

dW = np.random.normal(loc=0.0, scale=np.sqrt(dt), size=N)
W = np.cumsum(dW)
Ytrue = np.zeros(t.size)
Ytrue[0] = Xzero
Ytrue[1:] = Xzero * exp((alpha - 0.5 * beta ** 2) * t[1:] + beta * W[1:])

pl.plot(t, Ytrue, color="k", lw=0.8, label="True")

Yem = np.zeros(N)

Yem[0] = Xzero

for i in range(1, t.size):
    Yem[i] = Yem[i-1] + alpha * Yem[i-1] * dt + beta * Yem[i-1] * dW[i]
plt.plot(t, Yem, lw=0.8, label="EM")

emerr = np.abs(Yem[-1] - Ytrue[-1])
print("error is : ", emerr)
# print(Ytrue[0], Yem[0])
pl.legend()
pl.savefig("test_EM.png")
pl.close()
# plt.show()
