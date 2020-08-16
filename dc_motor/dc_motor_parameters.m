%Inductance
L=1;
%Resistance
R=1;
% back EMF coefficient
k_e=0.1;
% current to force coefficient
k_m=0.5;
%Motor Inertia
J_d=0.1;
%Load Inertia
J_m=0;
% friction coefficient
k_f=0.2;
% load momentum
M_d=0;

%coefficients of model
T=L/R;
K_D=1/R;
J=J_d+J_m;
dead_zone=3;

% State space canonical matrices, output is a velocity
Av=[0 1; -(R*k_f+k_m*k_e)/(L*J) -(L*k_f+R*J)/(L*J)];
Bv=[0; k_m/(L*J)];
Cv=[1 0];

% Canonical state space matrices, output is an angle
Aa=[0 1 0; 0 0 1; 0 -(R*k_f+k_m*k_e)/(L*J) -(L*k_f+R*J)/(L*J)];
Ba=[0; 0; k_m/(L*J)];
Ca=[1 0 0];

% State space vector: angle, velocity, current
A=[0 1 0; 0 -k_f/J k_m/J; 0 -k_e/L -R/L];
B=[0; 0; 1/L];
C=[1 0 0];
x0=[0;0;0];






