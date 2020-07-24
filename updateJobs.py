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

def retrieveData():
    print('finally some good fucking food')
schedule.every(10).seconds.do(retrieveData)


while 1:
    schedule.run_pending()
    time.sleep(1)