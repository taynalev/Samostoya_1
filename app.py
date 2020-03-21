import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
from dash.dependencies import Input, Output


colors = {
    'background': '#D2BEE9',
    'text': '#000080'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Приветсвую на сайте Татьяны Лёвиной :3',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-family': "Helvetica"
        }
    ),


    html.Div(children='Друзья называбт меня Таина или Тая - просто потому что мне не нравится сокращение Таня.', style={
        'textAlign': 'center',
        'color': colors['text'],
        'font-family': "Times New Roman"
    }),
    dcc.Markdown('''
                 **Поэтому во всех соцестях, например, [вк](https://vk.com/tainalev) меня зовут Таина.**''',style={
        'textAlign': 'center',
        'color': colors['text']
        }),
    html.Div([
            html.Img(src='https://lh3.googleusercontent.com/proxy/47wPbOC_Jl-J_kxlyArJXT6F3x593ZPzORUfP-qbwJ8xodcFmpvnAlVOboqxxTWQ7OBfpcEKrzcRX2Iycntx7tMw39q2ba7XswaNng',style={
'width':'75%', 'margin-left':150, 'margin-top':30, 'textAlign': 'center'})
            ]),


    html.Label('Люблю котиков!'),


    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Забавные штуки, которые я умею', value='tab-1'),
        dcc.Tab(label='Интересные для развития направления', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Играть на варгане, разбираться в архитектурных стилях и немного в современном искусстве, проводить эксурсии (даже диплом есть!), готовить сложные муссовые десерты')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Хочу освоить скалалазание и поставить голос, но больше всего (!) - нормально программировать хотя бы на питончике и освоить биоинформатику :)')
        ])
    

app.layout = html.Div([
    daq.LEDDisplay(
        id='my-LED-display',
        label="Default",
        value=6
    ),
    dcc.Slider(
        id='my-LED-display-slider',
        min=0,
        max=10,
        step=1,
        value=10
    ),
])


@app.callback(
    dash.dependencies.Output('my-LED-display', 'value'),
    [dash.dependencies.Input('my-LED-display-slider', 'value')]
)
def update_output(value):
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)
    app.run_server(debug=True)
