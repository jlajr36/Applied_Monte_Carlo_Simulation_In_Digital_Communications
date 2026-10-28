% Clear the Command Window
clc;

% Clear all variables from the workspace
clear;

% Set the number of bits to simulate
N = 10000;

% Set the signal amplitude
A = 1;

% Set the SNR values in decibels
SNR_dB = [0 3 6 12];

% Generate N random bits (0 or 1)
bits = randi([0 1], 1, N);

% Plot the first 100 random bits
figure;
stem(1:100, bits(1:100));
xlabel('Bit Number');
ylabel('Bit Value');
title('First 100 Random Bits');
ylim([-0.5 1.5]);
grid on;