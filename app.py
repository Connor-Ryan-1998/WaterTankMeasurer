import databaseFunctions as df
import datetime
import time
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import socket

##Server Configuration
host = socket.gethostbyname(socket.gethostname())
collection = df.Database(database="WaterTankIOT", collection="dbo.waterTankReadings").connectionString()
currentDateTime = datetime.datetime.now()
lookBackDateTime = datetime.timedelta(30)
reviewPeriod = currentDateTime - lookBackDateTime


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dataframe = df.Database(tank= "Tank01", readingDateTime={"$gt":reviewPeriod},collection = collection).queryTankData()
fig = go.Figure(data=[go.Scatter(x=dataframe['readingDateTime'], y=dataframe['reading'])])


app.layout = html.Div(style={'backgroundColor': '#111111'}, children=[
        dcc.Graph(
            id='sensorTimeSeries',
            figure=fig
        ),
        dcc.Interval(
            id='refresh',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )])


@app.callback(Output("sensorTimeSeries", "figure"), [Input("refresh", "n_intervals")])
def updateDataSource(n_intervals):
    dataframe = df.Database(tank= "Tank01", readingDateTime={"$gt":reviewPeriod},collection = collection).queryTankData()
    fig = go.Figure(data=[go.Scatter(x=dataframe['readingDateTime'], y=dataframe['reading'])])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host = host, port = 8050)
