import random

char = 'A'

ascii_val = ord(char)
print(f"Character: '{char}' -> ASCII Value: {ascii_val}")

binary_str = format(ascii_val, '08b')
print(f"8-bit Binary: {binary_str}")

# bits as integers
bits = [int(bit) for bit in binary_str]
print(f"Bit List: {bits}")

# Map to BPSK symbols (-1 and +1)
symbols = [2 * b - 1 for b in bits]
print(f"BPSK Symbols: {symbols}")

sigma = 0.4

received_symbols = []
for s in symbols:
    noise = random.gauss(0.0, sigma)
    received_symbols.append(s + noise)

print("Received Volts: ", [round(val, 2) for val in received_symbols])

# Demod, volt above 0, '1', else below 0, '0'
detected_bits = [1 if val > 0 else 0 for val in received_symbols]
print(f"Detected Bits: {detected_bits}")

detected_bin_str = "".join(str(b) for b in detected_bits)
detected_char = chr(int(detected_bin_str, 2))
print(f"Recovered Char: '{detected_char}'")