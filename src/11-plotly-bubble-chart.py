import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('../dataset/mpg.csv')

data = [go.Scatter(          # start with a normal scatter plot
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=1.5*df['cylinders'])  # set the marker size
)]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis=dict(title='horsepower'),  # x-axis label
    yaxis=dict(title='mpg'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
