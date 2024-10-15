#GOPH 419
#Lab 1
#Viktor Pejic
#30149473
import numpy as np
import math




def launch_angle_range(ve_v0, alpha, tol_alpha):


    min_alpha = (1 + tol_alpha) * alpha

    max_alpha = (1 - tol_alpha) * alpha

    phi = launch_angle(ve_v0, alpha)

    phi_range = np.array([launch_angle(ve_v0, max_alpha), launch_angle(ve_v0, min_alpha)])

    return phi_range, phi

def launch_angle(ve_v0, alpha):

    term = 1 - (alpha / (1 + alpha)) * (ve_v0 ** 2)

    if term < 0:
        print(f"Warning: Invalid term under the square root. Setting sin_phi to 0.")
        return 0

    sin_phi = (1 + alpha) * (term ** 0.5)
    angle = inv_sin(sin_phi)

    return angle

def sin_angle(ve_v0, alpha):
    term = 1 - (alpha / (1 + alpha)) * (ve_v0 ** 2)

    if term < 0:
        print(f"Warning: Invalid term for alpha={alpha}: {term}. Setting sin_phi to 0.")
        return 0

    sin_phi = (1 + alpha) * (term ** 0.5)
    return sin_phi

def inv_sin(x):

    result = 0.0
    eps_a = 1.0
    n = 1
    tol = 1e-8
    n_max = 100

    while eps_a > tol and n < n_max:

        term = ((2 * x) ** (2 * n)) / ((n ** 2) * (math.factorial(2*n) / (math.factorial(n) ** 2)))

        result += term

        if result != 0:
            eps_a = abs(term / result)
        else:
            eps_a = float('inf')

        n += 1

    result = np.sqrt(0.5 * result)
    return result

def arcsin(ve_v0, alpha, tol_alpha):

    expected_phi_range = np.array([np.asin(sin_angle(ve_v0, (1 - tol_alpha) * alpha)), np.asin(sin_angle(ve_v0, (1 + tol_alpha) * alpha))])
    expected_phi = np.asin(sin_angle(ve_v0, alpha))


    return expected_phi_range, expected_phi

def error(expected_phi_range, expected_phi, phi_range, phi):
    error_range = abs(expected_phi_range - phi_range)
    error_value = abs(expected_phi - phi)

    print (f"\nError range = {error_range}")
    print(f"Error value = {error_value}")

def main():
    ve_v0 = 2

    alpha = 0.25

    tol_alpha = 0.04

    if ve_v0 != 0 and 0 < alpha < 1:

        launch_angle_range(ve_v0, alpha, tol_alpha)
        arcsin(ve_v0, alpha, tol_alpha)

        expected_phi_range, expected_phi = arcsin(ve_v0, alpha, tol_alpha)
        phi_range, phi = launch_angle_range(ve_v0, alpha, tol_alpha)

        print(f"\nCalculated maximum and minimum launch angle = {phi_range}")
        print(f"Calculated launch angle = {phi}")

        print(f"\nExpected maximum and minimum launch angle = {expected_phi_range}")
        print(f"Expected launch angle = {expected_phi}")

        error(expected_phi_range, expected_phi, phi_range, phi)
    else:
        print(f"ValueError: Your input: ve_v0 = {ve_v0},\talpha = {alpha}\n\nInvalid ve_v0 or alpha value. Make sure ve_v0 does not equal 0\nand alpha is between 0 and 1.\n")
        quit()

if __name__ == "__main__":
    main()
