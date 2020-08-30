from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Inductance
L = 1
# Resistance
R = 1
# back EMF coefficient
k_e = 0.1
# current to force coefficient
k_m = 0.5
# Motor Inertia
J_d = 0.1
# Load Inertia
J_m = 0
# friction coefficient
k_f = 0.2
# Resulting inertia
J = J_d + J_m
# Input Voltage
U = 5

def dc_motor(state, time, parameters):
    phi, omega, I = state
    L, R, k_e, k_m, k_f, J, U = parameters
    dstate_dt = [omega,
                 k_m/J*I-k_f/J*omega,
                 1/L*U-k_e/L*omega-R/L*I
                ]
    return dstate_dt


t = np.linspace(0,20, 100)
parameters = [L, R, k_e, k_m, k_f, J, U]
state0 = [0, 0, 0]

result = odeint(dc_motor, state0, t, args=(parameters,))

plt.plot(t, result[:, 0], label='phi(t)')
plt.plot(t, result[:, 1], label='omega(t)')
plt.plot(t, result[:, 2], label='I(t)')
plt.xlabel('time')
plt.grid()
plt.legend(loc='best')
plt.show()



