"""
This module calculates quantities for one-dimensional freefall motion
"""
__author__ = "William Parker"

import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# URL of NASA Planetary Fact Sheet
URL = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"


def get_planetary_data():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return {}

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the main table that contains planetary data
    tables = soup.find_all("table")
    print(f"Number of tables found: {len(tables)}")

    # Assuming the table of interest is the second one
    planetary_table = tables[1] if len(tables) > 1 else tables[0]
    if not planetary_table:
        print("Could not find the planetary data table")
        return {}

    object_data = {}

    # Find all rows in the table
    rows = planetary_table.find_all("tr")

    for row in rows:
        print(row.find_all("td")[0].get_text()[:6])
        print()
    # Extract header and data
    # headers = [td.get_text(strip=True) for td in rows.find_all("td")]
    # print(headers)
    gravity_index = headers.index("Gravity (m/s²)") if "Gravity (m/s²)" in headers else -1

    if gravity_index == -1:
        print("Could not find Gravity column")
        return {}

    # Extract data rows
    for row in rows[1:]:
        columns = row.find_all("td")
        if len(columns) > gravity_index:
            name = columns[0].text.strip()
            gravity = columns[gravity_index].text.strip()

            # Convert gravity to float if possible
            try:
                gravity = float(gravity)
            except ValueError:
                gravity = None

            object_data[name] = gravity

    return object_data


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
    # object_data = {'Earth': 9.8, 'Moon': 1.6, 'Mars': 3.7}  # surface gravity [m/s/s]
    # starting_velocity = 10  #  m/s
    # times = np.linspace(0, 5)
    # for planet_data in object_data.items():
    #     velocities = velocity_in_time(times, initial_velocity=starting_velocity,
    #                                   gravitational_acceleration=planet_data[1])
    #     plt.plot(times, velocities, label=planet_data[0])
    #
    # plt.text(0, velocities[-1], f'Initial velocity: {starting_velocity:.0f} m/s')
    # plt.xlabel("Time (s)")
    # plt.ylabel("Velocity (m/s)")
    # plt.legend()
    # plt.show()


    # Retrieve and store data
    object_data = get_planetary_data()

    # Print result
    # print(object_data)

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
