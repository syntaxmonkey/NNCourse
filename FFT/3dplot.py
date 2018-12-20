
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import fft2d

# Source: https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(0, fft2d.samplex, fft2d.samplex)
y = np.linspace(0, fft2d.sampley, fft2d.sampley)

X, Y = np.meshgrid(x, y)
#Z = f(X, Y)
Z=fft2d.results


'''
# Plot contour
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
'''
step=10
# Plot surface
ax = plt.axes(projection='3d')
Z=np.log(np.abs(Z) )**2
#ax.plot_surface(X, Y, Z, rstride=step, cstride=step,  cmap='viridis', edgecolor='none')
ax.contour3D(X, Y, Z, 20, cmap='binary')
#ax.plot_wireframe(X, Y, Z, rstride=step, cstride=step, color='black')

#ax.plot_surface(X, Y, Z, rstride=step, cstride=step)
ax.set_title('surface');

plt.show()