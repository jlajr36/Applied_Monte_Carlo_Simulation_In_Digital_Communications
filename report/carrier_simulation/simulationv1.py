import math
import matplotlib.pyplot as plt

bits = [1, 0, 1, 1, 0, 1, 0]    # binary data stream
sample_per_symbol = 200         # resolution
symbol_duration = 1.0           # seconds
carrier_freq = 3.0              # cycles per symbol

num_bits = len(bits)
total_samples = num_bits * sample_per_symbol
delta_time = (num_bits * symbol_duration) / total_samples

time = []
digital_signal = []
carrier = []
bpsk_signal = []

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

    bpsk_signal.append(nrz * c_point)

fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)

axes[0].plot(time, digital_signal, 'b', linewidth=2)
axes[0].set_ylabel("Binary Data", fontsize=11)
axes[0].set_yticks([0, 1])
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].set_ylim(-0.2, 1.2)

axes[1].plot(time, carrier, 'g', linewidth=1.5)
axes[1].set_ylabel("Carrier Wave", fontsize=11)
axes[1].grid(True, linestyle='--', alpha=0.6)

axes[2].plot(time, bpsk_signal, 'r', linewidth=1.5)
axes[2].set_ylabel("BPSK Signal", fontsize=11)
axes[2].set_xlabel("Time (s)", fontsize=11)
axes[2].grid(True, linestyle='--', alpha=0.6)

plt.suptitle("BPSK Simulation", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()