"""
This module calculates quantities for one-dimensional freefall motion
"""
__author__ = "William Parker"

import numpy as np
import matplotlib.pyplot as plt


def test_plot():

    # Line
    intercepts = [4, 3]
    x_bounds = np.array([-3, 8])
    x_values = np.linspace(x_bounds[0], x_bounds[1], 100)
    # y_bounds = -intercepts[1] * x_bounds / intercepts[0] + intercepts[1]
    y_values = -intercepts[1] * x_values / intercepts[0] + intercepts[1]

    # Circle
    radius = intercepts[0]
    angles = np.linspace(0, 2 * np.pi, 4)
    circle_xs = radius * np.cos(angles)
    circle_ys = radius * np.sin(angles)

    # plt.plot(x_bounds, y_bounds)
    plt.plot(x_values, y_values)
    plt.plot(circle_xs, circle_ys)
    plt.show()

    return


def velocity_in_time(time, initial_velocity=0, gravitational_acceleration=9.8):
    """
    Calculate v(t) = v0 - g t
    Author: William Parker
    :param time:
    :param initial_velocity:
    :param gravitational_acceleration:
    :return: initial_velocity - gravitational_acceleration * time
    """
    return initial_velocity - gravitational_acceleration * time


def height_in_time(time, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_height + initial_velocity * time - 0.5 * gravitational_acceleration * time**2


def velocity_in_height(height, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    height_change = height - initial_height
    if initial_velocity == 0.0:
        return np.sqrt(initial_velocity**2 - 2 * gravitational_acceleration * height_change)
    else:
        return np.sign(initial_velocity) * np.sqrt(initial_velocity**2 - 2 * gravitational_acceleration * height_change)


if __name__ == '__main__':
    test_plot()

    # print(f'Tests for freefall motion calculations:')
    # starting_velocity = 1
    # total_time = 1
    # starting_height = 1
    #
    # print(f'\tTest velocity_in_time:')
    # test_velocity = velocity_in_time(total_time, initial_velocity=starting_velocity)
    # print(f'\tv(t = {total_time} s, v0 = {starting_velocity} m/s) = {test_velocity:.2f} m/s\n')
    #
    #
    # print(f'\tTest height_in_time:')
    # test_height = height_in_time(total_time, initial_height=starting_height, initial_velocity=starting_velocity)
    # print(f'\ty(t = {total_time} s, y0 = {starting_height} m, v0 = {starting_velocity} m/s) = {test_height:.2f} m\n')
