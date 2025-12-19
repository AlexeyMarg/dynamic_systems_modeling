import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

tau_T = 3600
tau_leak = 900
tau_phase = 10
k = 0.068
beta_heat = 0.4
beta_press = 0.4

A11 = -1/tau_T
A21 = k/tau_phase
A22 = -(1/tau_phase + 1/tau_leak)

A = np.array([[A11, 0], 
              [A21, A22]])
B = np.array([[beta_heat, 0],
              [0, beta_press]])
C = np.eye(2)


def autoclave_dynamics(t, x, A, B, u):
    u_array = np.array(u).flatten()
    dxdt = A @ x + B @ u_array
    return dxdt

x0 = np.array([10.0, -5.0])
u_const = np.array([.01, .5])
startTime=0
endTime=500
dt = 0.1
timeSteps=int((endTime - startTime) / dt)
simulationTime=np.linspace(startTime,endTime,timeSteps)

sol = solve_ivp(
    lambda t, x: autoclave_dynamics(t, x, A, B, u_const),
    t_span=[startTime, endTime],
    y0=x0,
    t_eval=simulationTime,
    method='RK45',
    rtol=1e-8,
    atol=1e-10
)

time = sol.t
state = sol.y

plt.subplot(1, 2, 1)
plt.plot(time, state[0, :], 'b-', linewidth=2)
plt.xlabel('Time [s]')
plt.ylabel('ΔT [°C]')
plt.title('Temperature error')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)


plt.subplot(1, 2, 2)
plt.plot(time, state[1, :], 'r-', linewidth=2)
plt.xlabel('Time [s]')
plt.ylabel('ΔP [bar]')
plt.title('Pressure error')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)

plt.show()

