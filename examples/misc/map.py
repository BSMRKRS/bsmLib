from bsmLib import map
from bsmLib import RPL

# Min/Max servo values
min = 1000
max = 2000

# Min/Max math values
math_min = -1
math_max = 1

# Math Value
val = 0 # Midpoint of math values

# Map math value to be in servo range of Min/Max
val = map(val, math_min, math_max, min, max) # Returns midpoint of servo values

# Write value to servo
RPL.servoWrite(0, val)
