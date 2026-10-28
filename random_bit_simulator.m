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

% Map bits to signal values: 0 -> +A, 1 -> -A
tx = A * (1 - 2 * bits);

% Plot the first 100 transmitted signal values
figure;
stem(1:100, tx(1:100));
xlabel('Bit Number');
ylabel('Signal Amplitude');
title('First 100 Transmitted Signal Values');
ylim([-1.5 1.5]);
grid on;

% Select the first SNR value (0 dB)
snr_db = SNR_dB(1);

% Convert SNR from decibels to a linear scale
snr_linear = 10^(snr_db / 10);

% Calculate the Gaussian noise variance
noise_var = A^2 / (2 * snr_linear);

% Generate Gaussian noise with zero mean
noise = sqrt(noise_var) * randn(1, N);

% Plot the first 100 Gaussian noise samples
figure;
stem(1:100, noise(1:100));
xlabel('Sample Number');
ylabel('Noise Amplitude');
title('First 100 Gaussian Noise Samples');
grid on;

% Add Gaussian noise to the transmitted signal
rx = tx + noise;

% Plot the first 100 received signal samples
figure;
stem(1:100, rx(1:100));
xlabel('Sample Number');
ylabel('Received Amplitude');
title('Received Signal with Gaussian Noise');
grid on;

% Detect bits using a zero decision threshold
bits_hat = rx < 0;

% Compare transmitted bits with detected bits
errors = bits ~= bits_hat;

% Count the total number of bit errors
num_errors = sum(errors);

% Calculate the bit error rate
BER = num_errors / N;

% Display the bit error rate
disp(BER);