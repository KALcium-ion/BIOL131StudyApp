# pages/welcome.py

from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

# List of topics
topics = [
    {"name": "Studying: A Guide", "path": "/blurt"},
    {"name": "Study Guide 1", "path": "/sg1"},
    {"name": "Study Guide 2", "path": "/sg2"},
    {"name": "Study Guide 3", "path": "/sg3"},
    {"name": "Study Guide 4", "path": "/sg4"}
]

# Layout with tutorial, top button, and study guide buttons
layout = html.Div([
    html.Img(
        src="/assets/WelcomePageWelcomeBanner.png",
        style={
            "width": "40%",  # Default to 100% width on small screens
            "maxWidth": "100%",
            "height": "auto",
            "display": "block",
            "margin": "0 auto"
        }
    ),
    dbc.Container([
        dbc.Card([
            dbc.CardBody([
                html.P(
                    [
                        "If you haven't visited our site before, please click on the ",
                        html.Strong("'Studying: A Guide' "),
                        "button to view a brief tutorial on how to make the most use out of this site!"
                    ],
                    className="card-text"
                ),
                html.P(
                    [
                        "If you are interested in learning more about different study techniques, please click on the ",
                        html.Strong("'Studying Techniques Overview'"),
                        " button!"
                    ],
                    className="card-text"
                ),
                html.P("Happy Studying!", className="card-text")
            ], style={'textAlign': 'left', 'fontSize': '20px'})
        ], className="mt-4 mb-4 shadow-sm")
    ]),

    # "How to Use This Site" button
    html.Div([
        dbc.Button(
            "Studying: A Guide",
            href="/how-to-use",
            color="light",  # Use a neutral base color
            size="lg",
            style={
                "margin": "20px",
                "textDecoration": "none",
                "display": "block",
                "marginLeft": "auto",
                "marginRight": "auto",
                "backgroundColor": "#588157",
                "color": "white",  # Optional: ensures white text for contrast
                "border": "none",  # Optional: remove Bootstrap border
                "fontSize":"20px",
                'padding':'5px',
                "borderRadius":"10px",
                "textAlign":"center",
                "fontFamily":"Arial"
            }
        )
    ]),

    html.Hr(style = {
        "borderTop":"2px solid #588157",
        "marginTop":"20px",
        "marginBottom":"20px"
    }),

    html.Div([
        html.H3("Study Guides:")
    ], style = {"fontSize":"20px",
                "fontFamily":"Arial", 
                "fontWeight": "bold"}),

    # Study guide buttons
    html.Div([
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        topic["name"],
                        href=topic["path"],
                        color="light",
                        size="lg",
                        style={
                            "margin": "20px",
                            "textDecoration": "none",
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto",
                            "backgroundColor": "#588157",
                            "color": "white",  # Optional: ensures white text for contrast
                            "border": "none",  # Optional: remove Bootstrap border
                            "fontSize":"20px",
                            'padding':'5px',
                            "borderRadius":"10px",
                            "textAlign":"center",
                            "fontFamily":"Arial"
                        }
                    )
                ) for topic in topics[1:]
            ],
            justify="around",
            align="center",
            style={"marginTop": "20px"}
        )
    ])
], style={
    'width': '80%',
    'marginTop': '20px',
    'marginLeft': 'auto',
    'marginRight': 'auto'
})
