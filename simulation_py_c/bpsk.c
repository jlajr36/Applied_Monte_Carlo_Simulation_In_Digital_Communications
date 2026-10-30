// Pseudo-code for your embedded loop
// while (1) {
//     for (int i = 0; i < 8; i++) {
//         if (symbols[i] > 0) {
//             set_dac_voltage(3.3); // High voltage state (+1 equivalent)
//         } else {
//             set_dac_voltage(0.0); // Low voltage state (-1 equivalent, using unipolar shift)
//         }
//         delay_ms(1); // Hold the voltage steady for 1 millisecond per bit
//     }
//     delay_ms(100); // Pause briefly before repeating the letter 'A'
// }

#include <stdio.h>

int main() {
    char letter = 'A';
    int bits[8];
    float symbols[8];

    printf("Character: '%c' -> ASCII Value: %d\n", letter, (unsigned char)letter);

    // 1. Extract the 8 bits using bitwise shifting
    // (letter >> (7 - i)) & 1 checks each bit from left to right
    for (int i = 0; i < 8; i++) {
        bits[i] = (letter >> (7 - i)) & 1;
    }

    // Print the bit array
    printf("Bit List:    [");
    for (int i = 0; i < 8; i++) {
        printf("%d%s", bits[i], (i < 7) ? ", " : "");
    }
    printf("]\n");

    // 2. Map bits to BPSK symbols (-1.0 and +1.0)
    for (int i = 0; i < 8; i++) {
        symbols[i] = 2.0f * (float)bits[i] - 1.0f;
    }

    // Print the symbol array
    printf("BPSK Symbols: [");
    for (int i = 0; i < 8; i++) {
        printf("%.0f%s", symbols[i], (i < 7) ? ", " : "");
    }
    printf("]\n");

    return 0;
}