import plotly.graph_objects as go


def Animation(curve, coords, *additional_curves):
    return go.Figure(
        data=[curve, curve, *additional_curves],
        layout=go.Layout(scene=dict(
            xaxis=dict(range=[-150, 150], autorange=False, zeroline=False),
            yaxis=dict(range=[-150, 150], autorange=False, zeroline=False),
            zaxis=dict(range=[0, 60], autorange=False, zeroline=False),
            hovermode="closest"),
            updatemenus=[dict(type="buttons",
                              buttons=[{
                                  "args": [None, {"frame": {"duration": 100, "redraw": True},
                                                  "fromcurrent": True, "transition": {"duration": 100,
                                                                                      "easing": "quadratic-in-out"}}],
                                  "label": "Play",
                                  "method": "animate"
                              },
                                  {
                                      "args": [[None], {"frame": {"duration": 0, "redraw": True},
                                                        "mode": "immediate",
                                                        "transition": {"duration": 0}}],
                                      "label": "Pause",
                                      "method": "animate"
                                  }],
                              direction="left",
                              pad={"r": 10, "t": 70})]),
        frames=[go.Frame(
            data=[go.Scatter3d(
                x=[coords[0][k]],
                y=[coords[1][k]],
                z=[coords[2][k]],
                mode="markers",
                marker=dict(color="red", size=5))])

            for k in range(100)]

    )
