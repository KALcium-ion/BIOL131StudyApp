import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import re
from studyguidedict import study_guides

def layout(sg, qid):
    return html.Div([
        dcc.Store(id="guide-qid-store", data={"sg": sg, "qid": qid}),  # Current guide & question
        html.Div(id="dynamic-question-content")
    ])

@dash.callback(
    Output("dynamic-question-content", "children"),
    Input("guide-qid-store", "data"),
)
def render_question_content(data):
    if not data:
        raise PreventUpdate

    guide = data.get("sg")
    qid = data.get("qid")

    # Validate inputs
    if not re.match(r'^sg[1-4]$', guide) or not re.match(r'^q\d+$', qid):
        raise PreventUpdate

    try:
        question_data = study_guides[guide]["questions"][qid]
    except KeyError:
        return dbc.Alert("Question not found.", color="danger")

    question_title = question_data.get("question", "No question available.")
    overview = question_data.get("overview", "No overview available.")
    deep_dive = question_data.get("deep_dive", "No deep dive available.")
    image_div = question_data.get("image", None)
    lecture_div = question_data.get("lecture", None)  # If you want to keep this tab, it will show full lecture content here.

    # Tab styles
    tab_style = {
        'background-color': '#a3b18a',
        'color': '#000',
        'font-weight': 'normal',
        'border-radius': '15px',
        'margin-right': '10px',
        'padding': '15px 30px',
        'border': 'none',
        'text-align': 'center',
        'font-size': '18px',
        'fontFamily':'Arial'
    }
    selected_tab_style = {
        'background-color': '#588157',
        'color': '#fff',
        'font-weight': 'bold',
        'font-size': '20px',
    }
    def get_tab_style(is_selected):
        return {**tab_style, **(selected_tab_style if is_selected else {})}

    tabs = dcc.Tabs(
        id="tabs",
        children=[
            dcc.Tab(label="Overview", value="overview", children=[html.Div(overview, style={'fontFamily':'Arial','fontSize':'18px','lineHeight':'1.6'})], style=get_tab_style(False), selected_style=get_tab_style(True)),
            dcc.Tab(label="Deep Dive", value="deep_dive", children=[html.Div(deep_dive, style={'fontFamily':'Arial','fontSize':'18px','lineHeight':'1.6'})], style=get_tab_style(False), selected_style=get_tab_style(True)),
            dcc.Tab(label="Image", value="image", children=[html.Div(image_div if image_div else html.P("No image available."), style={'maxWidth':'1800px','display':'flex','justifyContent':'center'})], style=get_tab_style(False), selected_style=get_tab_style(True)),
            dcc.Tab(label="Lecture Slides", value="lecture", children=[lecture_div if lecture_div else html.P("No lecture content available.")], style=get_tab_style(False), selected_style=get_tab_style(True))
        ],
        style={
            "marginBottom": "20px",
            "white-space": "nowrap",
            "overflow-x": "auto"
        }
    )

    nav_buttons = html.Div([
        dbc.Button("Back to Study Guide", href=f"/{guide}", style={"backgroundColor": "#3a5a40", "color": "white", "border": "none", 'fontWeight': 'bold', 'padding': '10px 20px', 'marginRight': '10px', 'borderRadius':'10px', 'textDecoration':'none', 'fontFamily':'Arial'}),
        dbc.Button("Back to Home", href="/", style={"backgroundColor": "#3a5a40", "color": "white", "border": "none", 'fontWeight': 'bold', 'padding': '10px 20px', 'borderRadius':'10px', 'textDecoration':'none', 'fontFamily':'Arial'}),
    ], style={"display": "flex", "justifyContent": "flex-start", "marginBottom": "20px"})

    start_buttons = html.Div([
        dbc.Button("Start Practice Quiz", href=f"/quiz/{guide}/{qid}", style={'backgroundColor':'#a3b18a','color':'#000','border':'none','fontWeight':'normal','borderRadius':'15px','padding':'15px 30px','fontSize':'18px','marginRight':'10px','textDecoration':'none','fontFamily':'Arial'}),
        dbc.Button("Start Guided Study", href=f"/study/{guide}/{qid}", style={'backgroundColor':'#a3b18a','color':'#000','border':'none','fontWeight':'normal','borderRadius':'15px','padding':'15px 30px','fontSize':'18px','textDecoration':'none','fontFamily':'Arial'}),
    ], style={"display": "flex", "justifyContent": "flex-start", "marginBottom": "20px"})

    question_header = html.Div([
        html.Span("Study Guide Question: ", style={'fontFamily': 'Arial', 'fontSize': '24px', 'fontWeight': 'bold', 'marginRight': '10px'}),
        html.Span(question_title, style={'fontFamily': 'Arial', 'fontSize': '24px'})
    ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'})

    content = [
        nav_buttons,
        html.Hr(style={'border': 'none', 'borderTop': '2px solid #ccc', 'margin': '20px 0'}),
        start_buttons,
        question_header,
        html.Hr(style={'border': 'none', 'borderTop': '2px solid #ccc', 'margin': '20px 0'}),
        tabs
    ]

    return dbc.Container(content, style={'marginTop': '30px', 'fontFamily':'Arial', 'width':'80%', 'marginLeft':'auto', 'marginRight':'auto', 'marginBottom':'100px'})
