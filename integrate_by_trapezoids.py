def integrate_by_trapezoids(integrand_function, lower_bound, upper_bound, number_of_intervals):
    integral = 0
    interval = (upper_bound - lower_bound)/number_of_intervals
    for index in range(1, number_of_intervals):
        position_of_index = lower_bound + index * interval
        integral += 0.5*interval*(integrand_function(position_of_index)
                                  + integrand_function(position_of_index + interval))
    return integral


def first_power(x):
    return x


def second_power(x):
    return x**2


if __name__ == '__main__':
    interval_number = 100
    bounds = (0, 1)

    print(f'Testing f(x) = x from 0 to 1')
    print(f'    int(x, 0, 1)         = {0.5:8.5f}')
    sum_string = f'    sum(x, 0, 1, n={interval_number:4}) = ' \
               + f'{integrate_by_trapezoids(first_power, bounds[0], bounds[1], interval_number):8.5f}'
    print(sum_string)

    print(f'Testing f(x) = x^2 from 0 to 1')
    print(f'    int(x, 0, 1)         = {1/3:8.5f} ')
    sum_string = f'    sum(x, 0, 1, n={interval_number:4}) = ' \
                 + f'{integrate_by_trapezoids(second_power, bounds[0], bounds[1], interval_number):8.5f}'
    print(sum_string)

    from math import sin, pi
    bounds = (0, 2*pi)
    print(f'Testing f(x) = sin(x) from 0 to 2π')
    print(f'    int(x, 0, 2π)        = {0:8.5f} ')
    sum_string = f'    sum(x, 0, 1, n={interval_number:4}) = ' \
                 + f'{integrate_by_trapezoids(sin, bounds[0], bounds[1], interval_number):8.5f}'
    print(sum_string)