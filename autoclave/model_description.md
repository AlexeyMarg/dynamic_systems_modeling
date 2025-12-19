# Mathematical Model of an Industrial Autoclave

## 1. State-Space Representation

The system is described by a continuous-time linear state-space model:

$$
\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)
$$

where:
- $\dot{\mathbf{x}}(t)$ is the time derivative of the state vector
- $\mathbf{A}$ is the system matrix
- $\mathbf{B}$ is the input matrix
- $\mathbf{x}(t)$ is the state vector
- $\mathbf{u}(t)$ is the control input vector

## 2. Variables

### 2.1 State Vector

The state vector represents deviations from setpoints:

$$
\mathbf{x}(t) = \begin{bmatrix}
\Delta T(t) \\
\Delta P(t)
\end{bmatrix}
$$

where:
- $\Delta T(t)$: Temperature deviation from setpoint [°C]
- $\Delta P(t)$: Pressure deviation from setpoint [bar]

### 2.2 Control Input Vector

The control inputs are actuator signals:

$$
\mathbf{u}(t) = \begin{bmatrix}
u_{\text{heat}}(t) \\
u_{\text{press}}(t)
\end{bmatrix}
$$

where:
- $u_{\text{heat}}(t)$: Heating actuator signal [0-10 engineering scale]
- $u_{\text{press}}(t)$: Pressure actuator signal [0-10 engineering scale]

## 3. System Matrix $\mathbf{A}$

The system matrix captures the internal thermodynamics:

$$
\mathbf{A} = \begin{bmatrix}
-\frac{1}{\tau_T} & 0 \\
\frac{k}{\tau_{\text{phase}}} & -\frac{1}{\tau_p}
\end{bmatrix}
$$

where:
- $\tau_T = 3600\text{ s}$: Thermal inertia time constant
- $\tau_{\text{phase}} = 10\text{ s}$: Phase transition time constant
- $\tau_p$: Effective pressure time constant
- $k$: Thermodynamic coupling coefficient [bar/°C]

The effective pressure time constant is:

$$
\frac{1}{\tau_p} = \frac{1}{\tau_{\text{leak}}} + \frac{1}{\tau_{\text{phase}}}
$$

where $\tau_{\text{leak}} = 900\text{ s}$ is the pressure leakage time constant.

### 3.1 Physical Interpretation

The elements of $\mathbf{A}$ represent:

1. **$A_{11} = -\frac{1}{\tau_T}$**: Passive cooling dynamics
2. **$A_{21} = \frac{k}{\tau_{\text{phase}}}$**: Temperature-pressure coupling (fast phase transition)
3. **$A_{22} = -\frac{1}{\tau_p}$**: Pressure relaxation (leakage + equilibrium drive)

## 4. Input Matrix $\mathbf{B}$

The input matrix models actuator effectiveness:

$$
\mathbf{B} = \begin{bmatrix}
\beta_{\text{heat}} & 0 \\
0 & \beta_{\text{press}}
\end{bmatrix}
$$

where:
- $\beta_{\text{heat}} = 0.4$ °C/s per control unit
- $\beta_{\text{press}} = 0.4$ bar/s per control unit

## 5. Stochastic Model (LQG)

For systems with measurement noise:

$$
\begin{aligned}
\dot{\mathbf{x}}(t) &= \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) + \mathbf{w}(t) \\
\mathbf{y}(t) &= \mathbf{C}\mathbf{x}(t) + \mathbf{v}(t)
\end{aligned}
$$

where:
- $\mathbf{y}(t)$: Measurement vector
- $\mathbf{C} = \mathbf{I}_2$: Identity matrix (both states measured)
- $\mathbf{w}(t) \sim \mathcal{N}(0, \mathbf{Q})$: Process noise
- $\mathbf{v}(t) \sim \mathcal{N}(0, \mathbf{R})$: Measurement noise

## 6. Discrete-Time Implementation

For digital control, the model is discretized:

$$
\begin{aligned}
\mathbf{x}_{k+1} &= \mathbf{A}_d\mathbf{x}_k + \mathbf{B}_d\mathbf{u}_k \\
\mathbf{y}_k &= \mathbf{C}_d\mathbf{x}_k
\end{aligned}
$$

Using zero-order hold with sample time $T_s$:

$$
\begin{aligned}
\mathbf{A}_d &= e^{\mathbf{A}T_s} \\
\mathbf{B}_d &= \left(\int_0^{T_s} e^{\mathbf{A}\tau} d\tau\right)\mathbf{B}
\end{aligned}
$$

## 7. Key Relationships

### 7.1 Temperature Dynamics

$$
\frac{d(\Delta T)}{dt} = -\frac{1}{\tau_T}\Delta T + \beta_{\text{heat}}u_{\text{heat}}
$$

### 7.2 Pressure Dynamics

$$
\frac{d(\Delta P)}{dt} = \frac{k}{\tau_{\text{phase}}}\Delta T - \frac{1}{\tau_p}\Delta P + \beta_{\text{press}}u_{\text{press}}
$$

### 7.3 Cross-Coupling

The temperature-pressure coupling is:

$$
\frac{\partial \dot{P}}{\partial T} = \frac{k}{\tau_{\text{phase}}}
$$

This represents how temperature changes drive pressure changes through vapor-liquid equilibrium.

## 8. Model Characteristics

1. **MIMO System**: 2 inputs, 2 outputs, 2 states
2. **Cross-Coupled**: $A_{21} \neq 0$ creates inherent coupling
3. **Time Scale Separation**:
   - Temperature: Slow ($\tau_T = 3600$ s)
   - Pressure: Fast ($\tau_p \approx 9.9$ s)
4. **Actuator Decoupling**: $\mathbf{B}$ is diagonal (simplifying assumption)

## 9. Parameter Summary

| Parameter | Symbol | Value | Units | Description |
|-----------|--------|-------|-------|-------------|
| Thermal inertia | $\tau_T$ | 3600 | s | Heat loss time constant |
| Leakage inertia | $\tau_{\text{leak}}$ | 900 | s | Pressure leakage time constant |
| Phase transition | $\tau_{\text{phase}}$ | 10 | s | Vapor equilibrium time constant |
| Coupling coefficient | $k$ | 0.068 | bar/°C | Temperature-pressure sensitivity |
| Heating gain | $\beta_{\text{heat}}$ | 0.4 | °C/s | Actuator effectiveness |
| Pressure gain | $\beta_{\text{press}}$ | 0.4 | bar/s | Actuator effectiveness |

This model provides a simplified yet physically meaningful representation of autoclave thermodynamics suitable for control system design.