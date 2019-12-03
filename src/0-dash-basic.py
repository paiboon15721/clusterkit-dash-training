import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash()

df = pd.read_csv("../dataset/salaries.csv")
dfSumRole = df.groupby('Role').sum()
srCountRole = df['Role'].value_counts()

app.layout = html.Div(
    [
        dcc.Graph(
            id='bar',
            figure={
                'data': [go.Bar(x=df['Name'], y=df['Salary'])],
                'layout': {
                    'title': 'Barchart show each employee salary'
                }
            }
        ),
        html.Div(
            dcc.Graph(
                id='pie',
                figure={
                    'data': [go.Pie(labels=dfSumRole.index, values=dfSumRole['Salary'])],
                    'layout': {
                        'title': 'Pie chart show role summary of expense'
                    }
                }
            ),
            style={'width': '45%', 'display': 'inline-block'}
        ),
        html.Div(
            dcc.Graph(
                id='pie2',
                figure={
                    'data': [go.Pie(labels=srCountRole.index, values=srCountRole.values)],
                    'layout': {
                        'title': 'Pie chart show summary of role in organization'
                    }
                }
            ), style={'width': '45%', 'display': 'inline-block'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server()
