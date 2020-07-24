import databaseFunctions as df
import datetime
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import schedule
import time

collection = df.Database.connectionString("WaterTankIOT", "dbo.waterTankReadings")
date = datetime.datetime(2000,1,1,1)
dataframe = df.Database.queryTankData("Tank01",{"$gt":date},collection)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig = go.Figure(data=[go.Scatter(x=dataframe['readingDateTime'], y=dataframe['reading'])])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
