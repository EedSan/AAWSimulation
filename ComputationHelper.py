import math
import random

import numpy as np


def random_point_on_sphere_coords():
    z_coord_on_sphere = random.uniform(25, 45)
    parameter_q = random.uniform(0, np.pi * 2)
    x_coord_on_sphere = math.sqrt(10000 - 4 * math.pow(z_coord_on_sphere, 2)) * math.cos(parameter_q)
    y_coord_on_sphere = math.sqrt(10000 - 4 * math.pow(z_coord_on_sphere, 2)) * math.sin(parameter_q)
    # print(f'x, y, z on sphere: {x_coord_on_sphere, y_coord_on_sphere, z_coord_on_sphere}')
    return x_coord_on_sphere, y_coord_on_sphere, z_coord_on_sphere


def random_point_in_circle(point_for_target=(0, 0, 0)):
    circle_radius = 81
    alpha = 2 * math.pi * random.random()
    r = circle_radius * math.sqrt(random.random())
    x = -abs(r * math.cos(alpha)) if point_for_target[0] > 0 else abs(r * math.cos(alpha))
    y = -abs(r * math.sin(alpha)) if point_for_target[1] > 0 else abs(r * math.sin(alpha))
    return x, y


def pivot_point(start_point, end_point):
    """Coordinates for pivot point of Quadratic Bezier Curve"""
    return [0, 0, 70]


def generateParabolaProperties():
    for i in range(1):
        altitude = random.randint(45, 55)
        x_sign = random.randint(0, 1)
        y_sign = random.randint(0, 1)
        x_direct = random.randint(100, 200)
        y_direct = random.randint(100, 200)
        if x_sign == 1:
            x_direct = -x_direct
        if y_sign == 0:
            y_direct = -y_direct
        x_bias = random.randint(0, 50)
        y_bias = random.randint(0, 50)
        return [altitude, x_direct, y_direct, x_bias, y_bias]


def create_projectile_trajectory(start_point, junction_point, index_of_point):
    t_parameter = np.linspace(0, 1, index_of_point - 5)
    pivot = [start_point[0], start_point[0], 30]
    x = start_point[0] * (1 - t_parameter) ** 2 + 2 * t_parameter * (pivot[0]) * (1 - t_parameter) + junction_point[
        0] * t_parameter ** 2
    y = start_point[1] * (1 - t_parameter) ** 2 + 2 * t_parameter * (pivot[1]) * (1 - t_parameter) + junction_point[
        1] * t_parameter ** 2
    z = start_point[2] * (1 - t_parameter) ** 2 + 2 * t_parameter * (pivot[2]) * (1 - t_parameter) + junction_point[
        2] * t_parameter ** 2
    return x, y, z
