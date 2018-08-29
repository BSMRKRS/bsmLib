from bsmLib import vector
from math import pi

v0 = vector(10, 10) # Set vector (x, y) coordinates to (10, 10)
v1 = v0.copy() # Creates copy of v0

v2 = v0 + v1 # Add two vectors
v3 = v0 - v1 # Subtract two vectors

v4 = v0 * 2 # Multiply by scaler
v5 = v0 / 2 # divide by scaler

v5.setMag(10) # Set magnitude
v5.setHeading(pi) # Set heading

# Print Values of vector
print(v0)
print(v5)
