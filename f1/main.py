
# Binary
0b1001 = 2^3 * 1 + 2^0*1 # evaluates to 9

# Hex
0x3F = 16^1 * 3 + 16^0 * 15 = 63

type(0b1001) == int
type(0x342AF) == int
# Just a different integer representation python doesnt really care

# Number conversion
bin(0xABCD) = '0b1010101111001101'
int('0b1010101111001101', 2) = 43981 # Binary conversion to base 10
int("0xABCD", 16) = 43981 # HEX conervsion to base 10

# Decimal numbers
(10.5)_10 = 10^1 * 1 + 10^0 * 0 + 5 * 10^-1

# Doesnt work
a = 0b0101.01

# Do instead
aa = 0b0101 * 0.25
