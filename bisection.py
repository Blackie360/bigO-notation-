import math

def quadratic_equation(a, b, c, x):
    # Evaluate the quadratic equation: ax^2 + bx + c
    return a * x**2 + b * x + c

def bisection_method(a, b, c, lower_limit, upper_limit, error_tolerance, max_iterations):
    # Check if the function changes sign within the specified limits
    if quadratic_equation(a, b, c, lower_limit) * quadratic_equation(a, b, c, upper_limit) >= 0:
        print("The function does not change sign within the specified limits.")
        return None

    # Perform bisection iterations
    for i in range(max_iterations):
        mid_point = (lower_limit + upper_limit) / 2
        f_mid = quadratic_equation(a, b, c, mid_point)

        # Check if the mid-point is the root or if the error tolerance is reached
        if abs(f_mid) < error_tolerance:
            return mid_point

        # Update the interval based on the sign change
        if quadratic_equation(a, b, c, lower_limit) * f_mid < 0:
            upper_limit = mid_point
        else:
            lower_limit = mid_point

    print("The maximum number of iterations has been reached.")
    return None

# Get input from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
lower_limit = float(input("Enter the lower limit: "))
upper_limit = float(input("Enter the upper limit: "))
error_tolerance = float(input("Enter the error tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Find the root using the bisection method
root = bisection_method(a, b, c, lower_limit, upper_limit, error_tolerance, max_iterations)

# Print the result
if root is not None:
    print("The root of the quadratic equation is:", root)
else:
    print("Unable to find the root within the specified limits and iterations.")

