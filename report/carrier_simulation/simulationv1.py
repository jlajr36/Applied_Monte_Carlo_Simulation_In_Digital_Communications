import math
import random
import matplotlib.pyplot as plt

bits = [1, 0, 1, 1, 0, 1, 0]    # binary data stream
sample_per_symbol = 200         # resolution
symbol_duration = 1.0           # seconds
carrier_freq = 3.0              # cycles per symbol
noise_std = 0.6                 # standard deviation of AWGN noise

num_bits = len(bits)
total_samples = num_bits * sample_per_symbol
delta_time = (num_bits * symbol_duration) / total_samples

time = []
digital_signal = []
carrier = []
bpsk_signal = []
noisy_bpsk_signal = []

for i in range(total_samples):
    current_time = i * delta_time
    time.append(current_time)

    bit_index = int(current_time/symbol_duration)
    if bit_index >= num_bits:
        bit_index = num_bits - 1

    bit = bits[bit_index]
    digital_signal.append(bit)

    nrz = 1 if bit == 1 else -1

    c_point = math.cos(2 * math.pi * carrier_freq * (current_time / symbol_duration))
    carrier.append(c_point)

    clean_bpsk = nrz * c_point
    bpsk_signal.append(clean_bpsk)

    noise = random.gauss(0, noise_std)
    noisy_bpsk_signal.append(clean_bpsk + noise)

demodulated_signal = []
recovered_bits = []

for i in range(total_samples):
    product = noisy_bpsk_signal[i] * carrier[i]
    demodulated_signal.append(product)

for bit_index in range(num_bits):
    start = bit_index * sample_per_symbol
    end = start + sample_per_symbol

    integral = sum(demodulated_signal[start:end]) * delta_time

    if integral > 0:
        recovered_bits.append(1)
    else:
        recovered_bits.append(0)

recovered_signal = []

for bit in recovered_bits:
    recovered_signal.extend([bit] * sample_per_symbol)

fig, axes = plt.subplots(6, 1, figsize=(11, 11), sharex=True)

axes[0].plot(time, digital_signal, 'b', linewidth=2)
axes[0].set_ylabel("Binary Data", fontsize=10)
axes[0].set_yticks([0, 1])
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].set_ylim(-0.2, 1.2)

axes[1].plot(time, carrier, 'g', linewidth=1.5)
axes[1].set_ylabel("Carrier Wave", fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.6)

axes[2].plot(time, bpsk_signal, 'r', linewidth=1.5)
axes[2].set_ylabel("BPSK (Clean)", fontsize=10)
axes[2].grid(True, linestyle='--', alpha=0.6)

axes[3].plot(time, noisy_bpsk_signal, color='orange', linewidth=1)
axes[3].set_ylabel("BPSK (Noisy)", fontsize=10)
axes[3].grid(True, linestyle='--', alpha=0.6)

axes[4].plot(time, demodulated_signal, 'm', linewidth=1)
axes[4].set_ylabel("Product Signal", fontsize=10)
axes[4].grid(True, linestyle='--', alpha=0.6)

axes[5].plot(time, recovered_signal, 'k', linewidth=2)
axes[5].set_ylabel("Recovered Bits", fontsize=10)
axes[5].set_xlabel("Time (s)", fontsize=11)
axes[5].set_yticks([0, 1])
axes[5].grid(True, linestyle='--', alpha=0.6)
axes[5].set_ylim(-0.2, 1.2)

plt.suptitle(f"BPSK Simulation with AWGN (noise_std={noise_std})", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()