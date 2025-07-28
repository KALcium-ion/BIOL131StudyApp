import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import studyguidedict
import os 
import random

# --- Tab Styling ---
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

# Layout specific to the quiz page
def layout(sg, qid):
    study_guide = studyguidedict.study_guides.get(sg)
    if not study_guide:
        return html.Div("Study guide not found.")
    
    question_data = study_guide["questions"].get(qid)
    if not question_data:
        return html.Div("Question not found.")
    
    button_style = {
        'backgroundColor':'#3a5a40',
        'color':'white',
        'border':'none',
        'fontWeight':'bold',
        'borderRadius':'20px',
        'padding':'10px 20px',
        'fontSize':'18px',
        'textDecoration':'none',
        'fontFamily':'Arial',
        'marginRight':'10px'
    }

    nav_buttons = html.Div([
        dbc.Button("Back to Home", href = "/", style = button_style),
        dbc.Button("Back to Study Guide", href = f"/{sg}", style = button_style),
    ], style = {'display':'flex', 
                'justifyContent':'flex-start',
                'padding':'15px 20px',
                'backgroundColor':'#f8f9fa',
                'borderBottom':'1px solid #ddd',
                'position':'sticky',
                'top':'0',
                'zIndex':'1000'})
    
    # --- Static slides ---
    intro_slide = html.Div([
        html.H3("Let's get started!"),
        html.P("You will need the following items:"),
        html.Ul([
                    html.Li("Timer (analog, digital, whatever works for you)."),
                    html.Li("A blank sheet of paper. I like unlined paper, but it doesn't really matter."),
                    html.Li("A pen or pencil."),
                    html.Li("A pen or pencil in a different color.")
                ], style={'textAlign': 'left'}),
        html.P(["You will set a timer for ", html.Strong("5, 10, 15, or 20 minutes.")]),
        html.P("Read the following question and answer it as best you can from your memory. Write down everything you can remember and whatever you can think of that connects to the question."),
        html.P("When your timer is up, progress to the next page!"),
        html.P("Go to the next slide to view the study guide question."),
    ], style={"fontFamily": "Arial", "fontSize": "20px", "padding": "20px"})

    question_text = question_data.get("question", "No Question Text Provided.")
    question_slide = html.Div([
        html.H3("Study Guide Question:"), 
        html.P(question_text, style = {'fontWeight':'bold',
                                       'border':'2px solid #444',
                                       'borderRadius':'10px',
                                       'boxShadow':'2px 2px 8px rgba(0,0,0.1)',
                                       'maxWidth':'700px',
                                       'margin':'10px auto',
                                       'textAlign':'center'}),
        html.P(html.Strong("Progress to the next page when your timer has completed."))
    ], style = {'fontFamily':'Arial', 'fontSize':'20px', 'padding':'20px'})

    pre_work_check_slide = html.Div([
        html.H3("Now let's check your work!"),
        html.P("Take your pen/pencil of a different color and mark anything that you missed."),
        html.P("Please note that you do not need to write everything exactly how it is written here. It is best for your memory and learning for you to use your own words."),
        html.P("Progress to the next slide to see what you should have written down:"),
    ], style = {'fontFamily':'Arial', 'fontSize':'20px', 'padding':'20px'})

    reflection_slide = html.Div([
        html.H2("Reflection Time"),
        html.P("Think about how confident you feel before you rate yourself."),
    ], style={"fontFamily": "Arial", "fontSize": "20px", "padding": "20px"})

    # --- Dynamic slides from dictionary ---

    def style_dynamic_slides(slide_list):
        styled = []
        for slide in slide_list:
            styled.append(
                html.Div(slide, style = {
                    'fontFamily':'Arial',
                    'fontSize':'22px',
                    'padding':'15px 0'
                })
            )
        return styled 
    
    blurting_from_dict = question_data.get("blurting", [])
    feynman_from_dict = question_data.get("feynman", [])

    # Default content if empty
    if not blurting_from_dict:
        blurting_from_dict = [html.P("No blurting content available.")]
    if not feynman_from_dict:
        feynman_from_dict = [html.P("No Feynman content available.")]

    blurting_from_dict = style_dynamic_slides(blurting_from_dict)
    feynman_from_dict = style_dynamic_slides(feynman_from_dict)

    # Combine static + dynamic slides
    blurting_slides = [intro_slide] + [question_slide] + [pre_work_check_slide] + blurting_from_dict + [reflection_slide]
    feynman_slides = [intro_slide] + [question_slide] + [pre_work_check_slide] + feynman_from_dict + [reflection_slide]

    return html.Div([
        nav_buttons,
        dcc.Tabs(
            id="study-method-tabs",
            value="blurting",
            children=[
                dcc.Tab(
                    label="Blurting",
                    value="blurting",
                    style=get_tab_style(False),
                    selected_style=get_tab_style(True),
                ),
                dcc.Tab(
                    label="Feynman",
                    value="feynman",
                    style=get_tab_style(False),
                    selected_style=get_tab_style(True),
                )
            ],
            style={
                "marginBottom": "20px",
                "white-space": "nowrap",
                "overflow-x": "auto",
            }
        ),

        html.Div(id="slideshow-container"),

        html.Div([
            html.Button("Previous", id="prev-btn", n_clicks=0),
            html.Button("Next", id="next-btn", n_clicks=0)
        ], style={"marginTop": "20px"}),

        # Hidden stores to track slide index and content
        dcc.Store(id="current-index", data=0),
        dcc.Store(id="blurting-content", data=blurting_slides),
        dcc.Store(id="feynman-content", data=feynman_slides),

        # Store for rating messages
        dcc.Store(id="rating-message", data=""),

        # Rating section with RadioItems (shown only on 3rd slide)
        html.Div([
            html.H4("Rate yourself on a scale of 1–5", style = {'fontFamily':'Arial', 'fontSize':'20px'}),
            dcc.RadioItems(
                id='rating-radio',
                options=[
                    {'label': "1 - It went bad. Basically a blank paper.", 'value': 1},
                    {'label': "2 - It went ok. I had some of the major concepts, but none of the details.", 'value': 2},
                    {'label': "3 - Not bad! I had most of the major concepts, but only some of the details.", 'value': 3},
                    {'label': "4 - Pretty good! I had all the major concepts, and most of the details.", 'value': 4},
                    {'label': "5 - Excellent! I had all the major concepts and pretty much all of the details!", 'value': 5}
                ],
                value=None,
                labelStyle={'display': 'block', 'marginBottom': '10px', 'fontFamily': 'Arial', 'fontSize': '18px'}
            ),
            html.Div(id="rating-message-container", children="")
        ], id="rating-container", style={'display': 'none'})
    ])


@dash.callback(
    Output("slideshow-container", "children"),
    Output("current-index", "data"),
    Output("prev-btn", "disabled"),
    Output("next-btn", "disabled"),
    Output("rating-container", "style"),
    Output("rating-message-container", "children"),
    Input("next-btn", "n_clicks"),
    Input("prev-btn", "n_clicks"),
    Input("study-method-tabs", "value"),
    Input("rating-radio", "value"),
    State("current-index", "data"),
    State("blurting-content", "data"),
    State("feynman-content", "data")
)
def update_slideshow(next_clicks, prev_clicks, tab, rating, index, blurting_data, feynman_data):
    ctx = dash.callback_context
    triggered_id = ctx.triggered_id if ctx.triggered_id else None

    # Select content based on the current tab
    data = blurting_data if tab == "blurting" else feynman_data
    max_index = len(data) - 1

    if triggered_id == "next-btn" and index < max_index:
        index += 1
    elif triggered_id == "prev-btn" and index > 0:
        index -= 1
    elif triggered_id == "study-method-tabs":
        index = 0  # Reset index on tab change

    prev_disabled = index == 0
    next_disabled = index == max_index

    rating_message_content = ""

    if index == len(data) - 1 and rating is not None:
        messages = {
                1: "You selected 1: No worries! This is a starting point. Space your review out over the next few days and use active recall to rebuild your memory. Don’t just reread. Test yourself again soon.",
                2: "You selected 2: You're on the path. Focus on the major concepts first, and revisit them in a few spaced sessions. Try using blurting or teaching it to someone else to reinforce retention.",
                3: "You selected 3: Nice progress! You’ve got a good grasp on the core ideas. Next time, mix in questions from different topics (interleaving) and test yourself again tomorrow to help it stick.",
                4: "You selected 4: Well done! You understand the key material. Come back to this in a few days for a quick test. Remember, spacing your recall strengthens memory. Try combining this with a different topic to boost interleaving effects.",
                5: "You selected 5: Excellent! You’re retaining both concepts and details. Keep that memory strong by testing again later this week. Mixing it with other topics will make it more flexible and durable.",
        }

        message_text = messages.get(rating, "")

        image_folder = os.path.join("assets", "feedback_images")
        try:
            image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            if image_files:
                selected_image = random.choice(image_files)
                image_path = f"/assets/feedback_images/{selected_image}"
                image_element = html.Img(src=image_path, style={'height': '300px', 'marginLeft': '20px', 'marginRight': '25px'})
            else:
                image_element = html.Div()
        except Exception as e:
            image_element = html.Div(f"Error loading image: {str(e)}")

        rating_message_content = html.Div([
            html.Div([
                image_element,
                html.Span(message_text)
            ], style={'display': 'flex', 'alignItems': 'center'})
        ], style={
            'border': '2px solid #ccc',
            'borderRadius': '10px',
            'padding': '15px',
            'margin': '20px auto',
            'fontFamily': 'Arial',
            'fontSize': '20px',
            'boxShadow': '2px 2px 10px rgba(0,0,0, 0.1)',
            'maxWidth': '700px',
            'width': '90%'
        })

    rating_container_style = {'display': 'block'} if index == len(data) - 1 else {'display': 'none'}

    return html.Div([data[index]]), index, prev_disabled, next_disabled, rating_container_style, rating_message_content
