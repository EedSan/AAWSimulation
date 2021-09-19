import plotly.graph_objects as go
import random
from AAWArea import sphere
from Aim import Aim


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
print(altitude, x_direct, y_direct, x_bias, y_bias)
aim = Aim.trajectoryEval(altitude, x_direct, y_direct, x_bias, y_bias)

layout = go.Layout(scene=dict(
    xaxis=dict(nticks=4, range=[-150, 150]),
    yaxis=dict(nticks=4, range=[-150, 150]),
    zaxis=dict(nticks=4, range=[0, 60]),
    aspectmode='manual',
    aspectratio=dict(x=1, y=1, z=0.3)),
    margin=dict(r=0, l=0, b=0, t=0))

fig = go.Figure(data=[zero_point, half_sphere, aim], layout=layout)
fig.show()

# ---- generate Aim
