"""
Functions for calculating minimum fluidization velocity, Umf.

Requirements:
Python 3, NumPy

Inputs:
ug = viscosity of gas, kg/ms
rhog = density of gas, kg/m^3
dp = diameter of bed particle, m
rhop = density of bed particle, kg/m^3
ep = void fraction, (-)
phi = sphericity of bed particle, (-)

Parameters:
a1, a2 = coefficients, (-)
g = gravity, m/s^2
Ar = Archimedes number, (-)
Re = Reynolds number, (-)

Output:
umf = minimum fluidization velocity, m/s

Reference:
Kunii and Levenspiel 1991. Fluidization engineering.
see pg. 69, 70 and Table 4
"""

# Modules
#------------------------------------------------------------------------------

import numpy as np

# Functions
#------------------------------------------------------------------------------

def umfWenYu(ug, rhog, dp, rhop):
    """
    Wen and Yu coefficients    
    """
    a1 = 33.7
    a2 = 0.0408
    g = 9.81

    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug)/(dp * rhog)
    
    return umf


def umfRich(ug, rhog, dp, rhop):
    """
    Richardson coefficients
    """
    a1 = 25.7
    a2 = 0.0365
    g = 9.81

    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug)/(dp * rhog)
    
    return umf


def umfSaxVog(ug, rhog, dp, rhop):
    """
    Saxena and Vogel coefficients
    """
    a1 = 25.3;
    a2 = 0.0571;
    g = 9.81

    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug)/(dp * rhog)
    
    return umf


def umfBabu(ug, rhog, dp, rhop):
    """
    Babu coefficients
    """
    a1 = 25.3;
    a2 = 0.0651;
    g = 9.81

    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug)/(dp * rhog)
    
    return umf


def umfGrace(ug, rhog, dp, rhop):
    """
    Grace coefficients
    """
    a1 = 27.2
    a2 = 0.0408
    g = 9.81

    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug)/(dp * rhog)
    
    return umf


def umfChit(ug, rhog, dp, rhop):
    """
    Chitester coefficients
    """
    a1 = 28.7
    a2 = 0.0494
    g = 9.81

    Ar = (g * dp**3 * rhog * (rhop - rhog)) / (ug**2)
    Re = (a1**2 + a2 * Ar)**0.5 - a1
    umf = (Re * ug)/(dp * rhog)
    
    return umf


def umfErgun(ug, rhog, dp, rhop, ep, phi):
    """
    Ergun function
    """
    g = 9.81
    
    a = 1.75 / (ep**3 + phi)
    b = 150*(1 - ep) / (ep**3 * phi)
    
    Ar = -((dp**3) * rhog * (rhop - rhog) * g) / (ug**2)
    Re = (-b + np.sqrt(b**2 - 4*a*Ar)) / (2*a)
    umf = (Re * ug) / (rhog * dp)
    
    return umf


def umfLargeRe(rhog, dp, rhop, ep, phi):
    """
    Large Reynolds number
    """
    g = 9.81
    umf = np.sqrt( (dp * (rhop - rhog) * g * ep**3 * phi) / (1.75 * rhog) )
    
    return umf


def umfSmallRe(ug, rhog, dp, rhop, ep, phi):
    """
    Small Reynolds number
    """
    g = 9.81
    umf = ((dp**2 *(rhop-rhog)*g)/(150 * ug)) * ((ep**3 * phi**2) / (1 - ep))
    
    return umf


