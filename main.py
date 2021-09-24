import math
import random

import numpy
import plotly.graph_objects as go

from AAWArea import sphere


def annotate(x_coord, z_coord, txt, x_anchor='center'):
    return dict(showarrow=False, x=x_coord, y=0, z=z_coord, text=txt, xanchor=x_anchor,
                font=dict(color='white', size=12))


def generateAimTrajectoryProperties():
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


zero_point = sphere(1, 1, "#000000", 1)
half_sphere = sphere(100, 50, '#ffff00', 0.2)
altitude, x_direct, y_direct, x_bias, y_bias = generateAimTrajectoryProperties()
# print(altitude, x_direct, y_direct, x_bias, y_bias)

layout = go.Layout(scene=dict(
    xaxis=dict(nticks=4, range=[-150, 150]),
    yaxis=dict(nticks=4, range=[-150, 150]),
    zaxis=dict(nticks=4, range=[0, 60]),
    aspectmode='manual',
    aspectratio=dict(x=1, y=1, z=0.3)),
    margin=dict(r=0, l=0, b=0, t=0))


# ---- choose random point on sphere

def random_point_on_sphere_coords():
    z_coord_on_sphere = random.uniform(25, 45)
    parameter_q = random.uniform(0, numpy.pi * 2)
    x_coord_on_sphere = math.sqrt(10000 - 4 * math.pow(z_coord_on_sphere, 2)) * math.cos(parameter_q)
    y_coord_on_sphere = math.sqrt(10000 - 4 * math.pow(z_coord_on_sphere, 2)) * math.sin(parameter_q)
    print(f'x, y, z on sphere: {x_coord_on_sphere, y_coord_on_sphere, z_coord_on_sphere}')
    return x_coord_on_sphere, y_coord_on_sphere, z_coord_on_sphere


def random_point_in_circle():
    circle_radius = 81
    alpha = 2 * math.pi * random.random()
    r = circle_radius * math.sqrt(random.random())
    x = r * math.cos(alpha)
    y = r * math.sin(alpha)
    return x, y


def pivot_point(start_point, end_point):
    return [(start_point[0] + end_point[0]), (start_point[1]),
            (start_point[2])]


# point_on_sphere = random_point_on_sphere_coords()
# point_on_sphere = go.Scatter3d(x=[point_on_sphere[0]],
#                                y=[point_on_sphere[1]],
#                                z=[point_on_sphere[2]],
#                                marker=dict(size=1, color='darkblue'),
#                                line=dict(color='darkblue', width=2))
#
# fig = go.Figure(data=[zero_point, half_sphere, point_on_sphere], layout=layout)
# fig.show()

target_start_point = random_point_on_sphere_coords()
target_end_point = random_point_in_circle() + (0,)
print(target_end_point)
target_pivot_point = pivot_point(target_start_point, target_end_point)


def bezier_quadratic_curve_coords(start_point, end_point, pivot_point):
    t_parameter = numpy.linspace(0, 1, 100)
    x = start_point[0] * (1 - t_parameter) ** 2 + \
        2 * t_parameter * (pivot_point[0] ** 2) * (1 - t_parameter) + \
        end_point[0] * t_parameter ** 2
    y = start_point[1] * (1 - t_parameter) ** 2 + \
        2 * t_parameter * (pivot_point[1] ** 2) * (1 - t_parameter) + \
        end_point[1] * t_parameter ** 2
    z = start_point[2] * (1 - t_parameter) ** 2 + \
        2 * t_parameter * (pivot_point[2] ** 2) * (1 - t_parameter) + \
        end_point[2] * t_parameter ** 2
    return x, y, z


bezier_curve = bezier_quadratic_curve_coords(target_start_point, target_end_point, target_pivot_point)

bezier_quadratic_curve = go.Scatter3d(x=bezier_curve[0],
                                      y=bezier_curve[1],
                                      z=bezier_curve[2],
                                      marker=dict(size=1, color='darkblue'),
                                      line=dict(color='darkblue', width=2))

fig = go.Figure(data=[bezier_quadratic_curve], layout=layout)
fig.show()
