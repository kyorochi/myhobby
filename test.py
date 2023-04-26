import matplotlib.pyplot as plt
import numpy as np
p = np.linspace( -4, 3, 10000)
q = p**5+p**4-10*p**3+2*p-8
plt.plot(p, q)
plt.show()
