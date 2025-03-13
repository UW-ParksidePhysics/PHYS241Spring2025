from freefall import velocity_in_height

moon_gravitational_acceleration = 1.1  # m/s/s
starting_height = 1  # m

velocity_at_ground = velocity_in_height(0, initial_height=starting_height,
                                        initial_velocity=0, gravitational_acceleration=moon_gravitational_acceleration)

print(
    f'v(y0 = {starting_height} m, v0 = 0, g={moon_gravitational_acceleration} m/s^2) = {velocity_at_ground:.2f} m/s\n')
