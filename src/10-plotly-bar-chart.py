import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../dataset/2018WinterOlympics.csv')

trace1 = go.Bar(
    x=df['NOC'],  # NOC stands for National Olympic Committee
    y=df['Gold'],
    name='Gold',
    marker=dict(color='#FFD700')  # set the marker color to gold
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker=dict(color='#9EA0A1')  # set the marker color to silver
)
trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker=dict(color='#CD7F32')  # set the marker color to bronze
)
data = [trace1, trace2, trace3]

layout = go.Layout(
    title='2018 Winter Olympic Medals by Country',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
