"""
ER Adds a line to commments, to see if Gavin sees this.....

Determine expanded bed height using the bed expansion factor.
Also compute the expanded bed void fraction.

Reference:
Santos 2010, Eq 14.7 and 14.8 on pg. 318, Eq 14.18 on pg. 320
"""

# Functions
#------------------------------------------------------------------------------

from funcFbexp import fbexp

# Parameters
#------------------------------------------------------------------------------

umf = 0.1157    # minimum fluidization velocity, m/s
u = 3.0*umf     # superficial gas velocity, m/s
db = 0.05232    # bed diameter, m
zmf = 0.1016    # bed height at minimum fluidizaiton, m
emf = 0.46      # void fraction at minimum fluidization
rhop = 2500     # density of bed particle, kg/m^3
dp = 0.0004     # diameter of bed particle, m
g = 9.81        # gravity, m/s^2
rhog = 0.4413   # density of gas, kg/m^3


# Bed Expansion Calculations
#------------------------------------------------------------------------------

# bed expansion factor
fbexp = fbexp(db, u, umf, rhog, rhop, dp)

# expanded bed height, zexp (m)
zexp = zmf*fbexp

# expanded bed void fraction from Eq 14.18
eexp = 1 - (1-emf)/fbexp

# Print Results
#------------------------------------------------------------------------------

print('')
print('zmf (m) =', zmf)
print('emf =', emf)
print('fbexp = ', fbexp)
print('zexp (m) =', zexp)
print('eexp =', eexp)
