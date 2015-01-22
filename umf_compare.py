"""
Compare Umf values from different correlations and equations.

Reference:
Kunii and Levenspiel 1991. Fluidization engineering.
see pg. 69, 70 and Table 4
"""

# Modules and Functions
#------------------------------------------------------------------------------

from funcUmf import umfBabu, umfChit, umfGrace, umfRich, umfSaxVog, umfWenYu
from funcUmf import umfErgun, umfLargeRe, umfSmallRe

# Parameters
#------------------------------------------------------------------------------

# particle properties
dp = 0.000207   # bed particle diameter, m
rhop = 2500     # density of bed particle, kg/m^3

# air properties at T=300K and P=1atm
# literature values for air viscosity can vary
# 1.846e-5 or 1.983e-5 or 1.73e-5 or 1.8568e-5 or 1.8531e-5 or 1.85e-5
ug = 1.983e-5   # dynamic viscosity of air, kg/ms
rhog = 1.17     # density of air, kg/m^3

# void fraction and sphericity for the Ergun equation
ep = 0.46   # void fraction, (-)
phi = 1.0   # sphericity, (-)

# Umf Calculations
#------------------------------------------------------------------------------

# Wen and Yu correlation
umf_WenYu = umfWenYu(ug, rhog, dp, rhop)

# Richardson correlation
umf_Rich = umfRich(ug, rhog, dp, rhop)

# Saxena and Vogel correlation
umf_SaxVogel = umfSaxVog(ug, rhog, dp, rhop)

# Babu correlation
umf_Babu = umfBabu(ug, rhog, dp, rhop)

# Grace correlation
umf_Grace = umfGrace(ug, rhog, dp, rhop)

# Chitester correlation
umf_Chit = umfChit(ug, rhog, dp, rhop)

# Ergun function
umf_Ergun = umfErgun(ug, rhog, dp, rhop, ep, phi)

# Small particles, Re < 20
umf_SmallRe = umfSmallRe(ug, rhog, dp, rhop, ep, phi)

# Large particles, Re > 1000
umf_LargeRe = umfLargeRe(rhog, dp, rhop, ep, phi)

# Print Results to Console
#------------------------------------------------------------------------------
print('Umf = {:.4f} m/s Wen and Yu'.format(umf_WenYu))
print('Umf = {:.4f} m/s Richardson'.format(umf_Rich))
print('Umf = {:.4f} m/s Saxena and Vogel'.format(umf_SaxVogel))
print('Umf = {:.4f} m/s Babu'.format(umf_Babu))
print('Umf = {:.4f} m/s Grace'.format(umf_Grace))
print('Umf = {:.4f} m/s Chitester'.format(umf_Chit))
print('Umf = {:.4f} m/s Ergun'.format(umf_Ergun))
print('Umf = {:.4f} m/s Small Re'.format(umf_SmallRe))
print('Umf = {:.4f} m/s Large Re'.format(umf_LargeRe))
