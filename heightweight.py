import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("height_weight.csv")
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist=False)
fig.show()