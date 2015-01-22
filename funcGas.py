"""
Calculate density and dynamic viscosity of a gas.
"""

def rhog(p, mw, T):
    """
    Calculate gas density
    
    Inputs:
    p = pressure (abs)
    mw = molecular weight of gas, g/mol
    T = temperature of gas, K
    
    Parameters:
    R = universal gas constant, L*kPa / K*mol
    
    Output:
    rhog = density of gas, kg/m^3
    """
    R = 8.3145
    rho = (p*mw) / (R*T)
    
    return rho


def mug():
    """
    work in progress...
    """
    return 2