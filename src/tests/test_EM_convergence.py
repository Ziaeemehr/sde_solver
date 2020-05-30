import numpy as np
import matplotlib.pyplot as plt
from numpy import exp
import pylab as pl

num_sims = 100  # Display five runs

T = 1
N = 2**15
dt = T / N
Xzero = 1.0
alpha = 2.0
beta = 1.0
t = np.arange(0, T, dt)

emerr = 0.0
for _ in range(num_sims):
    dW = np.random.normal(loc=0.0, scale=np.sqrt(dt), size=N)
    W = np.cumsum(dW)
    Xtrue = np.zeros(t.size)
    Xtrue[0] = Xzero
    Xtrue[1:] = Xzero * exp((alpha - 0.5 * beta ** 2) * t[1:] + beta * W[1:])
    Xem = np.zeros(N)
    Xem[0] = Xzero
    for i in range(1, t.size):
        Xem[i] = Xem[i-1] + alpha * Xem[i-1] * dt + beta * Xem[i-1] * dW[i]
    # plt.plot(t, Yem, lw=0.8)

    emerr += np.abs(Xem[-1] - Xtrue[-1])
print("error is : ", emerr / num_sims)
