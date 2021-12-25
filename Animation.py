import plotly.graph_objects as go


def Animation(target_curve, target_coords, text, projectile_coords, *additional_curves):
    frames = [go.Frame(data=[go.Scatter3d(x=[target_coords[0][k]], y=[target_coords[1][k]], z=[target_coords[2][k]],
                                          mode="markers", marker=dict(color="red", size=4)),
                             go.Scatter3d(x=[projectile_coords[0][k]], y=[projectile_coords[1][k]],
                                          z=[projectile_coords[2][k]], mode="markers",
                                          marker=dict(color="green", size=4))]) for k in
              range(min(len(target_coords[0]), len(projectile_coords[0])))]
    frames[33].layout.title = f'{text}'
    sliders = [{
        "pad": {"b": 10, "t": 60},
        "len": 0.9,
        "x": 0.1, "y": 0,
        "steps": [
            {
                "args": [[val], {
                    "frame": {"duration": 0},
                    "mode": "immediate",
                    "fromcurrent": True,
                    "transition": {"duration": 0, "easing": "linear"},
                }],
                "label": str(idx),
                "method": "animate",
            } for idx, val in enumerate(frames)
        ],
    }]
    layout = go.Layout(
        scene=dict(
            xaxis=dict(range=[-150, 150], autorange=False, zeroline=False),
            yaxis=dict(range=[-150, 150], autorange=False, zeroline=False),
            zaxis=dict(range=[0, 60], autorange=False, zeroline=False),
            hovermode="closest"),
        updatemenus=[dict(type="buttons",
                          buttons=[{
                              "args": [None, {"frame": {"duration": 50, "redraw": True},
                                              "fromcurrent": True, "transition": {"duration": 50,
                                                                                  "easing": "quadratic-in-out"}}],
                              "label": "Play",
                              "method": "animate"
                          }, {
                              "args": [[None], {"frame": {"duration": 0, "redraw": True},
                                                "mode": "immediate",
                                                "transition": {"duration": 0}}],
                              "label": "Pause",
                              "method": "animate"
                          }],
                          direction="left",
                          pad={"r": 10, "t": 70})],
        sliders=sliders,
    )
    return go.Figure(
        data=[target_curve, target_curve, target_curve, *additional_curves],
        layout=layout,
        frames=frames, )
