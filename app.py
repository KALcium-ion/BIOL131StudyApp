import dash
import os
from dash import html, dcc, Input, Output
from pages import sg1, sg2, sg3, sg4, questions, quizzes, welcome, study

#call the layout once to register callbacks from questions.py 
_ = questions.layout("sg1", "q1")

app = dash.Dash(__name__,
                suppress_callback_exceptions = True)
server = app.server #exposes the Flask server for Gunicorn 

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
        Output('page-content', 'children'), 
        Input('url', 'pathname')
    )

def display_page(pathname):
    if pathname == '/':
        return welcome.layout

    if pathname == '/sg1':
        return sg1.layout
    elif pathname == '/sg2':
        return sg2.layout
    elif pathname == '/sg3':
        return sg3.layout
    elif pathname == '/sg4':
        return sg4.layout
    
    if pathname.startswith('/studyguide/'):
        parts = pathname.strip('/').split('/')
        if len(parts) == 3:
            sg, qid = parts[1], parts[2]
            return questions.layout(sg, qid)

    if pathname.startswith('/quiz/'):
        parts = pathname.strip('/').split('/')
        if len(parts) == 3:
            sg, qid = parts[1], parts[2]
            return quizzes.layout(sg, qid)
        
    if pathname.startswith('/study/'):
        parts = pathname.strip('/').split('/')
        if len(parts) == 3:
            sg, qid = parts[1], parts[2]
            return study.layout(sg, qid)

    return html.H1("404 - Page not found")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host = "0.0.0.0", port=port)
