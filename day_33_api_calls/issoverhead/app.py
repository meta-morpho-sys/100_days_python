import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import logging as log
import iss_tracker as iss

app = dash.Dash()
server = app.server


app.layout = html.Div([
    html.H1("🛰️ ISS Live Tracker", style={"textAlign": "center", "color": "#444",}),
    html.Div([
         html.Button("ℹ️ ISS Info", id="toggle-info", n_clicks=0, style={
        "position": "absolute",
        "top": "20px",
        "left": "20px",
        "zIndex": 11
    }),
        # The info box (initially hidden)
        html.Div([
            html.H4("🛰️ ISS Tracker", style={"marginBottom": "5px"}),
            html.P(
                (
                    "The International Space Station (ISS) is a large space station that was assembled and is maintained in low Earth orbit by a collaboration of five space agencies and their contractors: NASA (United States), Roscosmos (Russia), ESA (Europe), JAXA (Japan), and CSA (Canada). "
                    "As the largest space station ever constructed, it primarily serves as a platform for conducting scientific experiments in microgravity and studying the space environment. (Source: Wikipedia)"
                ),
                style={"fontSize": "12px", "lineHeight": "1.5"}
            ),
            html.Ul([
                html.Li("Speed on orbit: 7.66 km/s"),
                html.Li("Max speed: 28,000 km/h"),
                html.Li("Orbit height: 408 km"),
                html.Li("Launch date: 20 November 1998")
            ],style={"fontSize": "12px", "lineHeight": "1.5"})
        ],
        id="info-box",
        style={
            "display": "none",
            "position": "absolute",
            "top": "70px",
            "left": "20px",
            "backgroundColor": "#f8f8f8",
            "padding": "15px",
            "border": "1px solid #ccc",
            "borderRadius": "8px",
            "width": "300px",
            "zIndex": 10
        })
    ]),

    dcc.Graph(id='iss-map'),
    html.H5("This map shows the real-time location  of the International Space Station (ISS).\n Updates every 60 seconds.",
            style={"textAlign": "center", "color": "red", "marginTop": "20px"}),
    html.P(
        "It is part of an app which tracks whether the International Space Station (ISS) is currently flying over your location at night and during clear skies — and notifies you via email when the conditions are just right to observe it.",
        style={
            "textAlign": "center",
            "maxWidth": "700px",
            "margin": "20px auto",
            "color": "#444",
            "fontSize": "14px",
            "lineHeight": "1.6"
        }
    ),

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
        textfont=dict(size=42),
        name="ISS"
    ))

    fig.update_layout(
        geo=dict(
            scope='world',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            showcountries=True,
            countrywidth=1,
            countrycolor='#8B0000',
            showocean=True,
            oceancolor="#9de5f5",
            lataxis_range=[-90, 90],
            lonaxis_range=[-180, 180],
            projection_type='natural earth'
        ),
        margin={"r":0,"t":0,"l":0,"b":0},
        height=600
    )
    return fig


@app.callback(
    Output("info-box", "style"),
    Input("toggle-info", "n_clicks"),
)
def toggle_info_box(n_clicks):
    base_style = {
        "position": "absolute",
        "top": "70px",
        "left": "20px",
        "backgroundColor": "#f8f8f8",
        "padding": "15px",
        "border": "1px solid #ccc",
        "borderRadius": "8px",
        "width": "300px",
        "zIndex": 10
    }

    if n_clicks and n_clicks % 2 == 1:
        # Show the box
        return {**base_style, "display": "block"}
    else:
        # Hide the box
        return {**base_style, "display": "none"}


if __name__ == "__main__":
    app.run(debug=True, port=8051)