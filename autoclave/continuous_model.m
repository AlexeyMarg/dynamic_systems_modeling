tau_T = 3600;
tau_leak = 900;
tau_phase = 10;
k = 0.068;
beta_heat = 0.4;
beta_press = 0.4;

A11 = -1/tau_T;
A21 = k/tau_phase;
A22 = -(1/tau_phase + 1/tau_leak);

A = [A11, 0; A21, A22];
B = [beta_heat, 0; 0, beta_press];
C = eye(2);

x0 = [10.0; -5.0];
u_const = [0.01; 0.5];

startTime = 0;
endTime = 500;
dt = 0.1;
timeSteps = floor((endTime - startTime) / dt);
simulationTime = linspace(startTime, endTime, timeSteps);

autoclave_ode = @(t, x) A * x + B * u_const;

[t, state] = ode45(autoclave_ode, simulationTime, x0);

state = state';

figure('Position', [100, 100, 800, 600]);

subplot(1, 2, 1);
plot(t, state(1, :), 'b-', 'LineWidth', 2);
xlabel('Time [s]');
ylabel('ΔT [°C]');
title('Temperature error');
grid on;
hold on;
yline(0, 'k--', 'Alpha', 0.5);

subplot(1, 2, 2);
plot(t, state(2, :), 'r-', 'LineWidth', 2);
xlabel('Time [s]');
ylabel('ΔP [bar]');
title('Pressure error');
grid on;
hold on;
yline(0, 'k--', 'Alpha', 0.5);
