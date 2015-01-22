"""
Bed expansion factor for calculating expanded bed height.

Reference:
Santos 2010, Eq 14.7 and 14.8 on pg. 318, Eq 14.18 on pg. 320
"""

def fbexp(db, u, umf, rhog, rhop, dp):
    """
    Inputs:
    db = diameter of bed, m
    u = superficial gas velocity, m/s
    umf = minimum fluidization velocity, m/s
    rhog = density of gas, kg/m^3
    rhop = density of bed particle, kg/m^3
    dp = diameter of bed particle, m
    Output:
    fbexp = bed expansion factor, (-)
    """
    if db < 0.0635:
        # diameter of bed as db < 0.0635 m from Eq 14.7
        tm1 = 1.032*((u-umf)**0.57)*(rhog**0.083)
        tm2 = (rhop**0.166)*(umf**0.063)*(db**0.445)
        fbexp = 1 + tm1/tm2
        return fbexp
    else:
        # diameter of bed as db >= 0.0635 m from Eq 14.8
        tm1 = 14.314*((u-umf)**0.738)*(dp**1.006)*(rhop**0.376)
        tm2 = (rhog**0.126)*(umf**0.937)
        fbexp = 1 + tm1/tm2
        return fbexp
    
    