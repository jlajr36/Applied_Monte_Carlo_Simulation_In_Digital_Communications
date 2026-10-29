
% Clear the Command Window
clc;

% Clear all variables from the workspace
clear;

% Close all open figure windows
close all;

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

% Prepare a vector to store the BER for each SNR value
BER_values = zeros(size(SNR_dB));

% Repeat the simulation for each SNR value
for k = 1:length(SNR_dB)

    % Select the current SNR value in decibels
    snr_db = SNR_dB(k);

    % Convert SNR from decibels to a linear scale
    snr_linear = 10^(snr_db / 10);

    % Calculate the Gaussian noise variance
    noise_var = A^2 / (2 * snr_linear);

    % Generate Gaussian noise with zero mean
    noise = sqrt(noise_var) * randn(1, N);

    % Add Gaussian noise to the transmitted signal
    rx = tx + noise;

    % Plot the first 100 received samples at 0 dB only
    if k == 1
        figure;
        stem(1:100, rx(1:100));
        xlabel('Sample Number');
        ylabel('Received Amplitude');
        title('Received Signal with Gaussian Noise at 0 dB');
        grid on;
    end

    % Detect bits using a zero decision threshold
    bits_hat = rx < 0;

    % Compare transmitted bits with detected bits
    errors = bits ~= bits_hat;

    % Count the total number of bit errors
    num_errors = sum(errors);

    % Calculate the bit error rate
    BER_values(k) = num_errors / N;

end

% Display the SNR and corresponding BER values
disp('SNR (dB)     BER');
disp([SNR_dB(:), BER_values(:)]);

% Plot BER versus SNR
figure;
semilogy(SNR_dB, BER_values, 'o-', 'LineWidth', 1.5);
xlabel('SNR (dB)');
ylabel('Bit Error Rate (BER)');
title('BER versus SNR');
xticks(SNR_dB);
xlim([0 12]);
grid on;