import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

scatterplot1 = dcc.Graph(id='scatterplot1',
                         figure={'data': [
                             go.Scatter(
                                 x=random_x,
                                 y=random_y,
                                 mode='markers',
                                 marker={
                                     'size': 12,
                                     'color': 'rgb(51,204,153)',
                                     'symbol': 'pentagon',
                                     'line': {'width': 2}
                                 }
                             )],
                             'layout': go.Layout(title='My Scatterplot',
                                                 xaxis={'title': 'Some X title'})}
                         )

scatterplot2 = dcc.Graph(id='scatterplot2',
                         figure={'data': [
                             go.Scatter(
                                 x=random_x,
                                 y=random_y,
                                 mode='markers',
                                 marker={
                                     'size': 12,
                                     'color': 'rgb(200,204,53)',
                                     'symbol': 'pentagon',
                                     'line': {'width': 2}
                                 }
                             )],
                             'layout': go.Layout(title='Second Plot',
                                                 xaxis={'title': 'Some X title'})}
                         )

app.layout = html.Div([scatterplot1, scatterplot2])

if __name__ == '__main__':
    app.run_server()
