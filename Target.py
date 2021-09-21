import numpy as np
import plotly.graph_objects as go


class Target:
    def __init__(self, x_coord, y_coord, z_coord,trajectory):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._z_coord = z_coord
        self._trajectory = trajectory


    @property
    def trajectory(self):
        return self._trajectory

    @property
    def x_coord(self):
        return self.x_coord

    @property
    def y_coord(self):
        return self.y_coord

    @property
    def z_coord(self):
        return self.z_coord


    @x_coord.setter
    def x_coord(self, value):
        self.x_coord = value

    @y_coord.setter
    def y_coord(self, value):
        self.y_coord = value

    @z_coord.setter
    def z_coord(self, value):
        self.z_coord = value

    @trajectory.setter
    def trajectory(self, value):
        self._trajectory = self.trajectoryEvalds(value[0], value[1], value[2], value[3], value[4])


    @staticmethod
    def trajectoryEval(altitude, x_direct, y_direct, x_bias, y_bias):
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

    @y_coord.setter
    def y_coord(self, value):
        self._y_coord = value
