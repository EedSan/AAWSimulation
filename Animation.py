import plotly.graph_objects as go


def Animation(curve, coords, *additional_curves):
    frames = Frames(coords)
    sliders = Sliders(frames)
    layout = go.Layout(
        scene=dict(
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
        data=[curve, curve, *additional_curves],
        layout=layout,
        frames=frames, )


def Frames(coords):
    return [go.Frame(data=[go.Scatter3d(x=[coords[0][k]], y=[coords[1][k]], z=[coords[2][k]],
                                        mode="markers", marker=dict(color="red", size=5))]) for k in range(100)]


def Sliders(frames):
    return [{
        "pad": {"b": 10, "t": 60},
        "len": 0.9,
        "x": 0.1, "y": 0,
        "steps": [
            {
                "args": [[val], frame_args(0)],
                "label": str(idx),
                "method": "animate",
            } for idx, val in enumerate(frames)
        ],
    }]


def frame_args(duration):
    return {
        "frame": {"duration": duration},
        "mode": "immediate",
        "fromcurrent": True,
        "transition": {"duration": duration, "easing": "linear"},
    }
