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

dt = 0.1;

sys_d = c2d(ss(A, B, C, zeros(2)), dt, 'zoh');
Ad = sys_d.A;
Bd = sys_d.B;

startTime = 0;
endTime = 500;
timeSteps = floor((endTime - startTime) / dt);
simulationTime = linspace(startTime, endTime, timeSteps+1);
u_const = [0.01; 0.5];
x0 = [10.0; -5.0];

state_history = zeros(2, length(simulationTime));
state_history(:, 1) = x0;

x = x0;
for i = 2:length(simulationTime)
    x = Ad * x + Bd * u_const;
    state_history(:, i) = x;
end

disp(['state_history.shape = [', num2str(size(state_history, 1)), ', ', num2str(size(state_history, 2)), ']']);

figure('Position', [100, 100, 800, 400]);

subplot(1, 2, 1);
plot(simulationTime, state_history(1, :), 'b-', 'LineWidth', 2);
xlabel('Time [s]');
ylabel('ΔT [°C]');
title('Temperature error');
grid on;
hold on;
yline(0, 'k--', 'Alpha', 0.5);

subplot(1, 2, 2);
plot(simulationTime, state_history(2, :), 'r-', 'LineWidth', 2);
xlabel('Time [s]');
ylabel('ΔP [bar]');
title('Pressure error');
grid on;
hold on;
yline(0, 'k--', 'Alpha', 0.5);