import plotly.graph_objects as go


def Animation(data):
    frames = framesList(data.get('Target Trajectory'))
    return go.Figure(
        data=[data.get('Target'), data.get('Target'), data.get('Half Sphere'), data.get('Zero Point')],
        layout=Layout(createSlider(frames)),
        frames=frames, )


def Layout(sliders):
    return go.Layout(
        scene=dict(
            xaxis=dict(range=[-150, 150], autorange=False, zeroline=False),
            yaxis=dict(range=[-150, 150], autorange=False, zeroline=False),
            zaxis=dict(range=[0, 60], autorange=False, zeroline=False), hovermode="closest"),
        updatemenus=[dict(type="buttons",
                          buttons=[dict(
                              args=[None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True,
                                           "transition": {"duration": 100, "easing": "quadratic-in-out"}}],
                              label="Play", method="animate"), dict(
                              args=[[None], {"frame": {"duration": 0, "redraw": True},
                                             "mode": "immediate", "transition": {"duration": 0}}],
                              label="Pause", method="animate")], direction="left", pad={"r": 10, "t": 70})],
        sliders=sliders,
        # annotations=annotations
    )


def framesList(coords):
    frames = []
    for k in range(len(coords[0])):
        frames.append(go.Frame(data=[go.Scatter3d(x=[coords[0][k]], y=[coords[1][k]], z=[coords[2][k]],
                                                  mode="markers", marker=dict(color="red", size=5))]))
    return frames


def createSlider(frames):
    return [dict(pad=dict(b=10, t=60), len=0.9, x=0.1, y=0, steps=[
        dict(args=[[val], frame_args(100)], label=str(idx), method="animate", ) for idx, val in enumerate(frames)], )]


def frame_args(duration):
    return dict(frame=dict(duration=duration), mode="immediate", fromcurrent=True,
                transition=dict(duration=duration, easing="linear"))

# def annotation(txt, xancr='center'):
#     return dict(showarrow=False, text=txt, xanchor=xancr)
