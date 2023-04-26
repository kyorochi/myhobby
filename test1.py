import numpy as np

import matplotlib.pyplot as plt

X0, X1, dx = -10, 11, 0.1

Y0, Y1, dy = -10, 11, 0.1

x=np.arange(X0,X1,dx)

y=np.arange(Y1,Y0,-dy)

x,y=np.meshgrid(x,y)

f=x*x+y*y-2*y*(abs(x)**(2.0/3.0))+abs(x)**(4.0/3.0
)

plt.figure(figsize=(10,10))

plt.contour(x,y,f)

plt.pcolormesh(x,y,f,shading='auto', cmap='spring')

plt.axis('off')

#plt.savefig('img/fld01b.png')

plt.show()