import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../dataset/2018WinterOlympics.csv')

data = [go.Bar(
    x=df['NOC'],  # NOC stands for National Olympic Committee
    y=df['Total']
)]
layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
