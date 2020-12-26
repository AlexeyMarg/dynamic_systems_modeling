from scipy.integrate import odeint
from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt

# Pendulum length
l = 1
# Pendulum mass
m = 1
# Cart mass
M = 1
# Grafity coefficient
g = 9.8


def inverted_pendulum_on_cart(state, time, parameters):
    theta, omega, x, v = state
    l, m, M, g = parameters
    F = 0  # external force applied to cart
    k=m/(m+M)
    dstate_dt = [omega,
                 (g*sin(theta)+cos(theta)*F/(m+M)-omega**2*k*l*cos(theta)*sin(theta))/(l-cos(theta)**2*k*l),
                 v,
                 (F+m*g*cos(theta)*sin(theta)+omega**2*m*l*sin(theta))/(m+M-cos(theta)**2*m)
                 ]
    return dstate_dt


t = np.linspace(0, 10, 100)
parameters = [l, m, M, g]
state0 = [pi/2, 0, 0, 0]

result = odeint(inverted_pendulum_on_cart, state0, t, args=(parameters,))

plt.plot(t, result[:, 0], label='theta(t)')
plt.plot(t, result[:, 1], label='omega(t)')
plt.plot(t, result[:, 2], label='x(t)')
plt.plot(t, result[:, 2], label='v(t)')
plt.xlabel('time')
plt.grid()
plt.legend(loc='best')
plt.show()
