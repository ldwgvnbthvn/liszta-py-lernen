
import math as m

# Keliling lingkaran
def circle_perimeter(radius):
    keliling = 2*radius*m.pi
    return keliling

print("Keliling Lingkaran = ", circle_perimeter(2))

# Fungsi sigmoid
def sigmoid(x):
    sig = (1/(1+(m.e)**(-1)))
    return sig

print("Sigmoid of x = ", sigmoid(3))