import plotly.graph_objects as go

from AAWArea import sphere
from Animation import Animation
from ComputationHelper import random_point_on_sphere_coords, random_point_in_circle, pivot_point
from Target import bezier_quadratic_curve_coords

zero_point = sphere(1, 1, "#000000", 1)
half_sphere = sphere(100, 50, '#ffff00', 0.2)
# altitude, x_direct, y_direct, x_bias, y_bias = generateParabolaProperties()

layout = go.Layout(scene=dict(
    xaxis=dict(nticks=4, range=[-150, 150]),
    yaxis=dict(nticks=4, range=[-150, 150]),
    zaxis=dict(nticks=4, range=[0, 60]),
    aspectmode='manual',
    aspectratio=dict(x=1, y=1, z=0.3)),
    margin=dict(r=0, l=0, b=0, t=0))

target_start_point = random_point_on_sphere_coords()
target_end_point = random_point_in_circle() + (0,)
target_pivot_point = pivot_point(target_start_point, target_end_point)
bezier_curve = bezier_quadratic_curve_coords(target_start_point, target_end_point, target_pivot_point)

bezier_quadratic_curve = go.Scatter3d(x=bezier_curve[0],
                                      y=bezier_curve[1],
                                      z=bezier_curve[2],
                                      marker=dict(size=1, color='darkblue'),
                                      line=dict(color='darkblue', width=2))

fig = Animation(bezier_quadratic_curve, bezier_curve, half_sphere, zero_point)

fig.show()
