import dash
from dash import html, Input, Output, dcc
import studyguidedict
import random

# Layout specific to the quiz page
def layout(sg, qid):
    study_guide = studyguidedict.study_guides.get(sg)
    if not study_guide:
        return html.Div("Study guide not found.")
    
    question_data = study_guide["questions"].get(qid)
    if not question_data:
        return html.Div("Question not found.")
    
    practice_questions = study_guide["questions"].get(qid, {}).get("practice_questions", [])
    if not practice_questions:
        return html.Div("No practice questions available.")

    # Generate 10 random questions and store them in dcc.Store
    selected_questions = random.sample(practice_questions, min(10, len(practice_questions)))
    
    question_components = []
    for index, pq in enumerate(selected_questions):
        question_components.append(
            html.Div([ 
                html.H3(f"Q{index + 1}: {pq['question']}"),
                dcc.RadioItems(
                    id=f"question-{index}",
                    options=[{"label": option, "value": option} for option in pq["options"]],
                    value=None,
                    labelStyle={"display": "block",
                                'fontSize':'18px',
                                'lineHeight':'1.3'},
                    style={"marginBottom": "20px"}
                ),
                html.Div(id=f"feedback-{index}", style={"display": "none"})  # Feedback hidden initially
            ])
        )

    studyguide_name = f"Study Guide {sg[2:]}" if sg.startswith("sg") else "Study Guide"
    question_number = qid[1:] if qid.startswith("q") else "Question Number"

    return html.Div([
        dcc.Store(id="question-store", data=selected_questions),  # Store only the 10 selected questions
        dcc.Store(id="guide-qid-store", data={"sg": sg, "qid": qid}),
        
        html.Div([
            dcc.Link(
                html.Button("Back to Study Guide", id = "back-to-study-guide", n_clicks = 0, style = {'fontSize':'18px',
                                                                                                      'borderRadius':'5px',
                                                                                                      'padding':'5px',
                                                                                                      'backgroundColor':'#a3b18a',
                                                                                                      'width':'200px',
                                                                                                      'marginRight':'10px'}),
                href = f"/{sg}",
                style = {'textDecoration':'none'}                                   
            ),
            dcc.Link(
                html.Button("Back to Home", id = "back-to-home", n_clicks = 0, style = {'fontSize':'18px',
                                                                                        'borderRadius':'5px',
                                                                                        'padding':'5px',
                                                                                        'backgroundColor':'#a3b18a',
                                                                                        'width':'200px',
                                                                                        'marginRight':'10px'}),
                href = "/",
                style = {'textDecoration':'none'}
            )
        ], style = {'display':'flex',
                    'justifyContent':'left',
                    'gap':'10px',
                    'marginTop':'20px'}),

        html.Div([html.H2(f"Quiz for {studyguide_name}: Question #{question_number}")], style={'fontFamily':'Arial'}),
        html.Hr(style={'border': 'none', 'borderTop': '2px solid #ccc', 'margin': '20px 0'}),
        html.Div(id="question-container", children=question_components),
    
        # Wrap the buttons in a flex container
        html.Div([
            html.Button("Submit Quiz", id="submit-quiz", n_clicks=0, style={
                "fontSize": '18px',
                "borderRadius": '5px',
                "padding": '5px',
                "backgroundColor": "#a3b18a",
                "width": '200px',  # Makes the button take up equal space
                "marginRight": "10px"  # Adds space between buttons
            }),
            html.Button("Generate New Quiz", id="generate-new-quiz", n_clicks=0, style={
                "fontSize": '18px',
                "borderRadius": '5px',
                "padding": '5px',
                "backgroundColor": "#a3b18a",
                "width": '200px',  # Makes the button take up equal space
                "marginLeft": "10px"  # Adds space between buttons
            })
        ], style={
            'display': 'flex',
            'justifyContent': 'left', 
            'gap': '10px',  # Adds a gap between the buttons
            'marginTop': '20px'
        }),
    
        html.Div(id="practice-questions", children=[]),
        html.Div(id="quiz-result", style={"marginTop": "20px"})
    ], style={'fontFamily': 'Arial', 'width': '80%', 'margin': '0 auto', 'marginBottom':'100px'})


# Callback for checking answers and generating new quiz
@dash.callback(
    [
        Output(f"feedback-{i}", "children") for i in range(10)
    ] + [
        Output(f"feedback-{i}", "style") for i in range(10)
    ] + [
        Output("quiz-result", "children"),
        Output("question-store", "data"),  # Update stored questions if new quiz
        Output("question-container", "children")
    ],
    [
        Input(f"question-{i}", "value") for i in range(10)
    ] + [
        Input("submit-quiz", "n_clicks"),
        Input("generate-new-quiz", "n_clicks")
    ],
    [Input("question-store", "data")]
)

def check_answers(*inputs):
    ctx = dash.callback_context
    if not ctx.triggered:
        return [None] * 10 + [None] * 10 + [""] + [dash.no_update, dash.no_update]

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    selected_answers = inputs[:10]
    current_questions = inputs[12]

    if triggered_id == "submit-quiz":
        feedback = []
        styles = []
        score = 0
        total = len(current_questions)

        for i, selected in enumerate(selected_answers):
            correct = current_questions[i]["answer"]
            if selected == correct:
                feedback.append(
                    html.Div(f"Correct! The answer is: {correct}", style = {'fontFamily':'Arial', 
                                                                            'fontSize':'18px',
                                                                            'fontWeight':'bold'})
                )
                styles.append({"color": "green"})
                score += 1
            else:
                feedback.append(
                    html.Div(f"Incorrect. The correct answer was: {correct}", style = {'fontFamily':'Arial',
                                                                                       'fontSize':'18px',
                                                                                       'fontWeight':'bold'})
                )
                styles.append({"color": "red"})
        
        score_display = html.Div([html.Div(f"Your score: {score}/{total} ({(score/total)*100:.2f}%)")], style = {'fontFamily':'Arial',
                                                                                                                 'fontSize':'30px',
                                                                                                                 'fontWeight':'bold'})
        return feedback + styles + [score_display, dash.no_update, dash.no_update]

    elif triggered_id == "generate-new-quiz":
        new_questions = random.sample(current_questions, min(10, len(current_questions)))
        new_components = [
            html.Div([ 
                html.H3(f"Q{index + 1}: {pq['question']}"),
                dcc.RadioItems(
                    id=f"question-{index}",
                    options=[{"label": option, "value": option} for option in pq["options"]],
                    value=None,
                    labelStyle={"display": "block"},
                    style={"marginBottom": "20px"}
                ),
                html.Div(id=f"feedback-{index}", style={"display": "none"})
            ]) for index, pq in enumerate(new_questions)
        ]
        return [None] * 10 + [None] * 10 + [""] + [new_questions, new_components]

    return [None] * 10 + [None] * 10 + [""] + [dash.no_update, dash.no_update]
