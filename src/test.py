import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(scale=0.3, size=10000)
y = (1 / ((2 * np.pi) ** (1 / 2))) * np.exp((-(x - 0) ** 2) / (2 * (0.3 ** 2)))
plt.figure("first photo")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.plot(x, y, ".")
# plt.show()
x = (x for x in range(5))
y = [x for x in range(5)]
print(x, y)
m = np.arange(4)
print(len(np.matrix(m)))
print(np.matrix(m).shape)
print(sum(m))
