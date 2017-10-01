import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.figure(2)

axe1 = plt.subplot(211)
axe2 = plt.subplot(212)

x = np.linspace(0, 3, 1000)
for i in range(5):
    plt.figure(1)
    plt.plot(x, np.exp(i*x/3))
    plt.sca(axe1)
    plt.plot(x, np.sin(i*x))
    plt.sca(axe2)
    plt.plot(x, np.cos(i*x))

plt.show()