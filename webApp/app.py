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
currentDateTime = datetime.datetime.now()
lookBackDateTime = datetime.timedelta(30)
reviewPeriod = currentDateTime - lookBackDateTime
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Data configuration
collection = df.Database(database="WaterTankIOT", collection="dbo.waterTankReadings").connectionString()
collection2 = df.Database(database="WaterTankIOT", collection="dbo.waterTanks").connectionString()
#insertData = df.Tank(tank="tank01",collection=collection2,height=1750,diameter=2175,capacity=6498.69,usableCapacity=5000).insertNewTankData()
dataframe = df.Database(tank= "Tank01", readingDateTime={"$gt":reviewPeriod},collection = collection).queryTankData()
#(3.14*(2175/2)^2*1750)*1e-6 volume calc
dimensions = df.Tank(tank="tank01",collection = collection2).tankDimensions()


for x in dataframe['reading']:
    dataframe['percentFull'] = float(df.Tank(tank="tank01",collection=collection,height=dimensions['height'],diameter=x,reading=100).calcPercentFull())

print(dataframe)




app.layout = html.Div(style={'backgroundColor': '#111111'}, children=[
        dcc.Graph(
            id='sensorTimeSeries',
            figure=go.Figure(data=[go.Scatter(x=dataframe['readingDateTime'], y=dataframe['reading'], mode='lines',name='distance from top')])
        ),
        dcc.Interval(
            id='refresh',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )])


@app.callback(Output("sensorTimeSeries", "figure"), [Input("refresh", "n_intervals")])
def updateDataSource(n_intervals):
    dataframe = df.Database(tank= "Tank01", readingDateTime={"$gt":reviewPeriod},collection = collection).queryTankData()
    fig = go.Figure(data=[go.Scatter(x=dataframe['readingDateTime'], y=dataframe['reading'], mode='lines',name='distance from top')])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host = host, port = 8050)
