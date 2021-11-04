import dash
import plotly.graph_objects as go
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from AAWArea import sphere
from ComputationHelper import random_point_on_sphere_coords, random_point_in_circle, pivot_point
from Target import bezier_quadratic_curve_coords

zero_point = sphere(1, 1, "#000000", 1)
half_sphere = sphere(100, 50, '#ffff00', 0.2)

layout = go.Layout(scene=dict(xaxis=dict(nticks=4, range=[-150, 150]), yaxis=dict(nticks=4, range=[-150, 150]),
                              zaxis=dict(nticks=4, range=[0, 60]), aspectmode='manual',
                              aspectratio=dict(x=1, y=1, z=0.3)), margin=dict(r=0, l=0, b=0, t=0), height=900)

target_start_point = random_point_on_sphere_coords()
target_end_point = random_point_in_circle(target_start_point) + (0,)
bezier_curve = bezier_quadratic_curve_coords(target_start_point, target_end_point,
                                             pivot_point(target_start_point, target_end_point))

target_path = go.Scatter3d(x=bezier_curve[0], y=bezier_curve[1], z=bezier_curve[2],
                           marker=dict(size=1, color='darkblue'), line=dict(color='darkblue', width=2))

data = {'Target': target_path,
        'Target Trajectory': bezier_curve,
        'Half Sphere': half_sphere,
        'Zero Point': zero_point, }

frames = [go.Frame(name=n, data=[
    go.Scatter3d(x=[data.get('Target Trajectory')[0][n]], y=[data.get('Target Trajectory')[1][n]],
                 z=[data.get('Target Trajectory')[2][n]], mode="markers", marker=dict(color="red", size=2)),
    data.get('Target'), data.get('Zero Point'), data.get('Half Sphere'), ])
          for n in range(len(data.get('Target Trajectory')[0]))]

fig = go.Figure(data=frames[0].data, frames=frames, layout=layout)
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), )

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Div(children=[dcc.Slider(id="dashSlider", min=0, max=100, step=1, value=5,
                                  tooltip={"placement": "right", "always_visible": True}, vertical=False, ),
                       html.Button("Play", id="dashPlay", n_clicks=1),
                       dcc.Interval(id="animateInterval", interval=400, n_intervals=0, disabled=False),
                       dcc.Graph(id="graph", figure=fig,
                                 style={'width': '100%', 'height': '100%', 'padding-bottom': '0%'}), ]),
    html.Div(id="whichframe", children=[],
             style={'width': '10px', 'height': '10px', 'padding-bottom': '0%', 'display': 'inline-block',
                    'vertical-align': 'middle'}),
])


@app.callback(
    Output("whichframe", "children"),
    Output("graph", "figure"),
    Input("dashSlider", "value"),
)
def setFrame(frame):
    print(fig.frames[frame].name)
    if frame:
        figure = go.Figure(fig.frames[frame].data, frames=fig.frames, layout=layout)
        try:
            figure.layout['sliders'][0]['active'] = frame
        except IndexError:
            pass
        return frame, figure
    else:
        return 0, fig


@app.callback(
    Output("animateInterval", "disabled"),
    Input("dashPlay", "n_clicks"),
    State("animateInterval", "disabled"),
)
def play(n_clicks, disabled):
    return not disabled


@app.callback(
    Output("dashSlider", "value"),
    Input("animateInterval", "n_intervals"),
    State("dashSlider", "value")
)
def doAnimate(i, frame):
    if frame < (len(frames) - 1):
        frame += 1
    else:
        frame = 0
    return frame


# target = Target.Target()
# target.move()
# print(target.current)

app.run_server(debug=True, host="localhost", port=8050)

# fig = go.Figure(data=[bezier_quadratic_curve, half_sphere, zero_point])
# print(bezier_quadratic_curve)
# def var_name(var):
#     return [k for k, v in locals().iteritems() if v == var][0]
