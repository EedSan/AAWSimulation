import numpy as np
import plotly.graph_objects as go


class Target:
    def __init__(self, x_coord, y_coord, trajectory):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self._trajectory = trajectory

    @property
    def trajectory(self):
        return self._trajectory

    @trajectory.setter
    def trajectory(self, value):
        self._trajectory = self.trajectoryEval(value[0], value[1], value[2], value[3], value[4])

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
