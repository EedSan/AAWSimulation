import numpy as np
import plotly.graph_objects as go


def sphere(radius, height, color, opacity):
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi / 2, 100)

    x = radius * np.outer(np.cos(theta), np.sin(phi))
    y = radius * np.outer(np.sin(theta), np.sin(phi))
    z = height * np.outer(np.ones(100), np.cos(phi))

    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], opacity=opacity, showscale=False)
