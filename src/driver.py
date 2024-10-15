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

    print(f"\nMaximum and minimum launch angle = {phi_range}")
    print(f"\nExpected launch angle = {phi}")
    return phi_range

def launch_angle(ve_v0, alpha):

    term = 1 - (alpha / (1 + alpha)) * (ve_v0 ** 2)

    if term < 0:
        print(f"Warning: Invalid term under the square root. Setting sin_phi to 0.")
        return 0

    sin_phi = (1 + alpha) * (term ** 0.5)
    angle = inv_sin(sin_phi)

    return angle


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


def main():
    ve_v0 = (float(input("Enter the escape/terminal velocity ratio: ")))

    alpha = float(input("Maximum altitude as a fraction of Earth's radius : "))

    tol_alpha = float(input("Enter alpha tolerance : "))

    launch_angle_range(ve_v0, alpha, tol_alpha)

if __name__ == "__main__":
    main()
