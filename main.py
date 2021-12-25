import random
import numpy as np
import plotly.graph_objects as go
from AAWArea import sphere
from Animation import Animation
from ComputationHelper import random_point_on_sphere_coords, random_point_in_circle, pivot_point, \
    create_projectile_trajectory
from Target import bezier_quadratic_curve_coords

zero_point = sphere(1, 1, "#000000", 1)
half_sphere = sphere(100, 50, '#ffff00', 0.2)

layout = go.Layout(scene=dict(
    xaxis=dict(nticks=4, range=[-150, 150]),
    yaxis=dict(nticks=4, range=[-150, 150]),
    zaxis=dict(nticks=4, range=[0, 60]),
    aspectmode='manual',
    aspectratio=dict(x=1, y=1, z=0.3)),
    margin=dict(r=0, l=0, b=0, t=0))

target_start_point = random_point_on_sphere_coords()
target_end_point = random_point_in_circle(target_start_point) + (0,)
target_pivot_point = pivot_point(target_start_point, target_end_point)
bezier_curve = bezier_quadratic_curve_coords(target_start_point, target_end_point, target_pivot_point)
bezier_curve_line = go.Scatter3d(x=bezier_curve[0], y=bezier_curve[1], z=bezier_curve[2],
                                 marker=dict(size=1, color='darkblue'), line=dict(color='darkblue', width=2))

index_of_point = 30
j_point = [bezier_curve[0][index_of_point], bezier_curve[1][index_of_point], bezier_curve[2][index_of_point]]
junction_point = go.Scatter3d(x=[bezier_curve[0][index_of_point - 5]], y=[bezier_curve[1][index_of_point - 5]],
                              z=[bezier_curve[2][index_of_point - 5]],
                              marker=dict(size=3, color='green'))

projectile_points = create_projectile_trajectory((0, 0, 0), j_point, index_of_point)

if random.random() < 0.1:  # <- if miss  (if prob > 0.1 => hit successfully)
    projectile_points = np.concatenate((np.zeros((3, (round(random.random()) * 10))), projectile_points), axis=1)
    delta_x = projectile_points[0][-2] - projectile_points[0][-1]
    delta_y = projectile_points[1][-2] - projectile_points[1][-1]
    delta_z = projectile_points[2][-2] - projectile_points[2][-1]
    for i in range(len(bezier_curve[0] - len(projectile_points[0]))):
        if i < 5:
            a = [projectile_points[0][-1] - delta_x, projectile_points[1][-1] - delta_y,
                 projectile_points[2][-1] - delta_z]
        else:
            a = [projectile_points[0][-1], projectile_points[1][-1], projectile_points[2][-1]]
        b = np.array([a]).T
        projectile_points = np.concatenate([projectile_points, b], axis=1)
    new_bezier_curve = bezier_curve
    # print(projectile_points)
    title_text = 'Fail'
else:  # <- if hit
    projectile_points = np.concatenate((np.zeros((3, 6)), projectile_points), axis=1)
    title_text = 'Success'
    new_bezier_curve = []
    for i in bezier_curve:
        new_bezier_curve.append(i[:index_of_point + 1])

projectile_trajectory = go.Scatter3d(x=projectile_points[0], y=projectile_points[1], z=projectile_points[2],
                                     marker=dict(size=1, color='blue'), line=dict(color='blue', width=2))

fig = Animation(bezier_curve_line, new_bezier_curve, title_text, projectile_points, half_sphere, zero_point, )

fig.show()
