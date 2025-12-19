import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import cont2discrete
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

dt = 0.1
sys_d = cont2discrete((A, B, C, np.zeros(shape=(2,2))), dt, method='zoh')
Ad = np.array(sys_d[0])
Bd = np.array(sys_d[1])

startTime=0
endTime=500
timeSteps=int((endTime - startTime) / dt)
simulationTime=np.linspace(startTime,endTime,timeSteps)
u_const = np.array([[.01], 
                    [.5]])
x0 = np.array([[10.0], 
               [-5.0]])

state_history = np.zeros((2, len(simulationTime)))
state_history[:, 0:1] = x0  # Записываем начальное состояние

# Дискретное моделирование (прямая Euler-подобная схема)
x = x0.copy()
for i in range(1, len(simulationTime)):
    # Дискретное уравнение: x[k+1] = Ad·x[k] + Bd·u[k]
    x = Ad @ x + Bd @ u_const
    state_history[:, i:i+1] = x
    
    
print(state_history.shape)

plt.subplot(1, 2, 1)
plt.plot(simulationTime, state_history[0, :], 'b-', linewidth=2)
plt.xlabel('Time [s]')
plt.ylabel('ΔT [°C]')
plt.title('Temperature error')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)


plt.subplot(1, 2, 2)
plt.plot(simulationTime, state_history[1, :], 'r-', linewidth=2)
plt.xlabel('Time [s]')
plt.ylabel('ΔP [bar]')
plt.title('Pressure error')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)

plt.show()
    
    
    