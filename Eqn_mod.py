# Imports the main parsing functions from sympy
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,\
                                        implicit_multiplication_application)
from sympy import Eq

def get_parsed(eqn): # Parses what the user imputs allowing for mathematical notation

    # Replaces e with exp(1) because e is considered a special character and will not be evaluated as the constant unless this is done
    # Replaces ^ with ** to allow for exponents with ^
    eqn = eqn.replace("e", "exp(1)").replace("^", "**")

    # Allows for implicit multiplication notation(2x)
    # Allows the trig functions to be expressed without parens "cos x)

    # Sets the transformations on the equation
    transformations = standard_transformations + (implicit_multiplication_application,)

    # Actually makes them here
    parsed = parse_expr(eqn, transformations = transformations)



    
    return parsed # Returns a parsed string that can be solved in equations



