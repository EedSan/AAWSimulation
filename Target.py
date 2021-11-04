from time import sleep
import numpy as np
import plotly.graph_objects as go
from ComputationHelper import random_point_on_sphere_coords, random_point_in_circle, pivot_point

triggered = False


class Target:
    def __init__(self):
        self.current = random_point_on_sphere_coords()
        self.__finish = random_point_in_circle() + (0,)
        self._trajectory = bezier_quadratic_curve_coords(self.current, self.__finish,
                                                         pivot_point(self.current, self.__finish))
        self.speed = None  # todo

    def move(self):
        if triggered:
            for elem in self._trajectory:
                self.current = elem
                # print(self.current)
                sleep(1000)

    def returnTrajectory(self):
        return self._trajectory

    @property
    def trajectory(self):
        return self._trajectory

    @trajectory.setter
    def trajectory(self, value):
        self._trajectory = self.trajectoryEval(value[0], value[1], value[2], value[3], value[4])

    @staticmethod
    def trajectoryEval(altitude, x_direct, y_direct, x_bias, y_bias):
        """create target trajectory as parabola"""
        x = np.linspace(-x_direct + x_bias, x_direct + x_bias, 100).tolist()
        y = np.linspace(-y_direct + y_bias, y_direct + y_bias, 100).tolist()
        z = [(-(i ** 2) / 100 + altitude) for i in x]

        x_curve = list()
        y_curve = list()
        z_curve = list()

        for idx, val in enumerate(z):
            if z[idx] >= 0:
                z_curve.append(z[idx])
                x_curve.append(x[idx])
                y_curve.append(y[idx])

        return go.Scatter3d(x=x_curve, y=y_curve, z=z_curve, marker=dict(size=1, color='darkblue'),
                            line=dict(color='darkblue', width=2))


def bezier_quadratic_curve_coords(start_point, end_point, pivot_point):
    t_parameter = np.linspace(0, 1, 100)
    x = start_point[0] * (1 - t_parameter) ** 2 + \
        2 * t_parameter * (pivot_point[0]) * (1 - t_parameter) + \
        end_point[0] * t_parameter ** 2
    y = start_point[1] * (1 - t_parameter) ** 2 + \
        2 * t_parameter * (pivot_point[1]) * (1 - t_parameter) + \
        end_point[1] * t_parameter ** 2
    z = start_point[2] * (1 - t_parameter) ** 2 + \
        2 * t_parameter * (pivot_point[2]) * (1 - t_parameter) + \
        end_point[2] * t_parameter ** 2
    return x, y, z
