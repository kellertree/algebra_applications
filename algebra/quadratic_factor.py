# application for factoring quadratic equations.

import math

def factor_quadratic(a, b, c):

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if discriminant is negative, zero, or positive
    if discriminant < 0:
        # One real root (perfect square)
        root = -b / (2 * a)
        return f"The quadratic has oen real root: (x - {root})^2"
    else:
        # Two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The quadratic can be factored as (x - {root1})(x - {root2})"
    
a, b, c = 2, -4, -6
print(factor_quadratic(a, b, c))