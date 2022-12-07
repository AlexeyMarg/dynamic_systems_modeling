m = 1; % mass

%Inertia
Ix = 1;
Iy = 1;
Iz = 1;
Ixy = 0.2;
Ixz = 0;
Iyz = 0;

% Mass center
x_c = 0;
y_c = 0.005;

% Motor parameters
k_m = 1;
T_m = 0.1;
C_m = 0.07; % coefficient motor to inertia momentum

% Initial conditions
q0 = [0; 0; 0; 0; 0; 0];

% Geometry
a = 0.1;
b = 0.42;
L_kr = 0.533;
phi_kr1 = 60 *pi / 180;
phi_kr2 = 36.05 *pi / 180;

Lx = b/2 + L_kr / sqrt(1 + tan(phi_kr1)^2 + tan(phi_kr1)^2);
Ly = L_kr / sqrt(1 + tan(phi_kr1)^2 + tan(phi_kr1)^2) * tan(phi_kr2);
Lz = a/2 + L_kr / sqrt(1 + tan(phi_kr1)^2 + tan(phi_kr1)^2) * tan(phi_kr1);

% For forcesп
rho = 1.22; % плотность воздуха
D = 0.55; % диаметр винта
Cdv = 0.02; %коэффициен тпересчета тяги двигателей в момент инерции

M = [m 0 0 0 0 0;
     0 m 0 0 0 0;
     0 0 m 0 0 0;
     0 0 0 Ix -Ixy 0;
     0 0 0 -Ixy Iy 0;
     0 0 0 0 0 Iz];


