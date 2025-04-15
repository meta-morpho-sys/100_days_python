import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import logging as log
import iss_tracker as iss

app = dash.Dash()
server = app.server


app.layout = html.Div([
    html.H1("🛰️ ISS Live Tracker", style={"textAlign": "center"}),
    dcc.Graph(id='iss-map'),
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0)  # update every 60 seconds
])

@app.callback(
    Output('iss-map', 'figure'),
    Input('interval-component', 'n_intervals')
)

def update_iss_location(n):
    try:
        _, coordinates = iss.is_iss_near()
        lat = coordinates[0]
        lon = coordinates[1]
    except Exception as e:
        log.error(f"Error getting ISS location: {e}")
        lat, lon = 0, 0  # fallback to center

    fig = go.Figure(go.Scattergeo(
        lat=[lat],
        lon=[lon],
        mode='text',
        text=["🛰"],
        textfont=dict(size=38),
        name="ISS"
    ))

    fig.update_layout(
        geo=dict(
            scope='world',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            showcountries=True,
            lataxis_range=[-90, 90],
            lonaxis_range=[-180, 180],
        ),
        margin={"r":0,"t":0,"l":0,"b":0},
        height=600
    )
    return fig
