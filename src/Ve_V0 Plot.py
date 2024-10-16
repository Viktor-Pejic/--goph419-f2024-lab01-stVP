#GOPH 419
#Lab 1
#Viktor Pejic
#30149473
import numpy as np
import matplotlib.pyplot as plt
import math

def launch_angle_range(ve_v0, alpha, tol_alpha):


    min_alpha = (1 + tol_alpha) * alpha

    max_alpha = (1 - tol_alpha) * alpha

    phi_range = np.array([launch_angle(ve_v0, max_alpha), launch_angle(ve_v0, min_alpha)])

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
    #print(result)
    return result




def main():

    tol_alpha = 0.04
    alpha = 0.25

    ve_v0_values = np.linspace(1.4, 2, 100)

    max_angles = []
    min_angles = []

    for ve_v0 in ve_v0_values:

        angles = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(angles[1])
        max_angles.append(angles[0])

    plt.figure(figsize=(10, 5))
    plt.plot(ve_v0_values, max_angles, label='Maximum angle', linewidth = 2)
    plt.plot(ve_v0_values, min_angles, label='Minimum angle', linewidth=2)

    plt.title('Minimum and Maximum Launch Angles vs. ve_v0')
    plt.xlabel('Ve/V0')
    plt.ylabel('Launch angle')
    plt.legend()

    plt.savefig('C:/Users/Viktor/Labs/Lab-1/figures/Min_and_Max_Angles_vs_VeV0.png')

    plt.show()

if __name__ == '__main__':
    main()
















