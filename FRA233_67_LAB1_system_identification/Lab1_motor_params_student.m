%{  
This script for prepare data and parameters for parameter estimator.
1. Load your collected data to MATLAB workspace.
2. Run this script.
3. Follow parameter estimator instruction.
%}

% Student's code  for collected data
load("data_signal\sin0d1.mat");
%load("data_signal\ramp1d2.mat");
%load("data_signal\pwm1.mat");
n_Sample = data{1}.Values.Length;

real_output = zeros(n_Sample, 1);
time = zeros(n_Sample, 1);


% R and L from experiment
motor_R = 5.54; % Ohm
motor_L = 0.0038; % Henry
% Optimization's parameters
motor_Eff = 0.5;
motor_Ke = 0.05;
motor_J = 0.001;
motor_B = 0.0001;

Input = data{1}.Values.Data;
Time = data{1}.Values.Time;
Velo = double(data{2}.Values.Data);

% Extract collected data
%{
Input = data{1}.Values.Data;
Time = data{1}.Values.Time;
Velo = double(data{2}.Values.Data);
%}

%real_output = Velo;
%time = Time;

% Plot 
figure(Name='Motor velocity response')
plot(Time,Velo,Time,Input)

