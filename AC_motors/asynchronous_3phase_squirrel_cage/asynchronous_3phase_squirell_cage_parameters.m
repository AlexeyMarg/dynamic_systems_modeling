% Asynchronous 3-phase squirell cage motor parameters
Z = 1; %Number of pole pairs
Ls = 0.1; % Stator inductance
Lr = 0.1; % Stator inductance
Lm = 0.05; % Stator and rotor cross inductance
Rs = 10; % Stator resistance
Rr = 10; % Stator resistance
J = 1; % Inertia momentum
M = 0; % External force momentum acting on rotor

%Some constants for model
Kr = Lm/Lr;
Tr = Lr/Rr;