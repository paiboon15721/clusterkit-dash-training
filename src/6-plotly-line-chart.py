import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv(
    '../dataset/population.csv',
    index_col=0)

traces = [go.Scatter(
    x=df.columns,
    y=df.loc[name],
    mode='markers+lines',
    name=name
) for name in df.index]

layout = go.Layout(
    title='Population Estimates of the Six New England States'
)

fig = go.Figure(data=traces, layout=layout)
pyo.plot(fig)
