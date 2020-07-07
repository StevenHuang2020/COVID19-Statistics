# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import datetime

import sys 
sys.path.append("..") 

from plotCoronavirous import pathsFiles

class layperOutClass:
    def __init__(self,app):
        print("-------------------init-----------------")
        self.app = app
        #self.color_lock = [ "#cce6ff", "#857aad", "#690a3d"]
        self.wroldData = self.getWorldData()
        self.AllCountries = self.getCountries()
        self.layerOut()
        
    def getWorldData(self):
        df = pd.read_csv(r'..\dataCountry\Worldwide.csv')
        #print(df.head(5))
        for col in df.columns: 
            df[col] = df[col].astype(str)
        return df

    def getCountryData(self,country):
        df = pd.read_csv(r'..\dataCountry\\' + country + '.csv')
        #print(df.head(5))
        for col in df.columns: 
            df[col] = df[col].astype(str)
        return df
    
    def getCountries(self):
        countries = []
        for i in pathsFiles(r'..\dataCountry\\','csv'):
            #print(i)
            country = i[i.rfind('\\')+1:i.rfind('.')]
            #print('country=',country)
            countries.append(country)
        return countries
       
    def layerOut(self):
        fig_lw = make_subplots(rows=2, cols=2, subplot_titles='COVID-19 statistics')
        
        dataWorld = self.wroldData.copy()
        #dataWorld = dataWorld.loc[:,['Date','Confirmed']]
        #dataWorld.set_index(["Date"], inplace=True)
        
        elment = go.Bar(x=dataWorld['Date'],y=dataWorld['Confirmed'], marker=dict(color="blue"), showlegend=False,text='World Confirmed cases')
        fig_lw.add_trace(elment, row=1, col=1)
        elment = go.Bar(x=dataWorld['Date'],y=dataWorld['Deaths'], marker=dict(color="red"), showlegend=False,text='World Deaths')
        fig_lw.add_trace(elment,row=1, col=2)
        elment = go.Bar(x=dataWorld['Date'],y=dataWorld['NewConfirmed'], marker=dict(color="yellow"), showlegend=False,text='World NewConfirmed')
        fig_lw.add_trace(elment,row=2, col=1)
        elment = go.Bar(x=dataWorld['Date'],y=dataWorld['NewDeaths'], marker=dict(color="black"), showlegend=False,text='World NewDeaths')
        fig_lw.add_trace(elment,row=2, col=2)
        fig_lw.update_layout(title_text="Wrold COVID-19 statistics") #height=400, width=600,
        fig_lw.update_layout(margin={'l': 20, 'b': 10, 't': 50, 'r': 0}, hovermode='closest')
        #fg = px.bar(dataWorld, x='Date', y='Confirmed', hover_data=['Deaths', 'Mortality'], #color='Deaths')
        
        dicts = []
        for i in self.AllCountries:
            dicts.append({'label':i,'value':i})
            
        #print(dicts)
        dropdownCountry = dcc.Dropdown(id="country_dropDown",options=dicts, value=dicts[0]['value'])  
        
        self.app.layout = html.Div([
                # adding a header and a paragraph
                html.Div([html.H2("COVID-19 statistics dashboard @StevenHuang2020"),
                html.P("Source reference:https://google.com/covid19-map/")], style = {'padding' : '50px' , 'backgroundColor' : '#3aaab2'}),
                html.Div(id="slideshow-container", children=[dcc.Graph(figure = fig_lw)], style = {'display': 'inline-block'}),
                #html.Div(id="country-dropDown", children=[dropdownCountry], style = {'display': 'inline-block'}),
                
                html.Div( id="country",
                        children=[html.Br(),html.Br(),
                        html.Label("Country COVID-19 statistics"),
                        dropdownCountry,
                        dcc.Graph(id='Country_NewCases')],  style = {
                                            'width' : '50%',
                                            'fontSize' : '20px',
                                            'padding-left' : '60px',
                                            'padding-right' : '100px',
                                            'display': 'inline-block'
                                            })
        ])

def setupApp(layer, app):
    @app.callback(Output('Country_NewCases', 'figure'),
                    [Input('country_dropDown', 'value')])

    def update_figure(country):
        print('country=',country)
        df = layer.getCountryData(country)
        #print(df.head(5))
        
        #dataWorld = layer.wroldData.copy()
        #fig = px.bar(dataWorld, x="Date", y="Confirmed", color="Confirmed", custom_data=["NewConfirmed"])
        if 0:
            fig = px.bar(df, x="Date", y="Confirmed")
        else:
            fig = make_subplots(rows=2, cols=2)
            fig.add_trace(go.Bar(x=df['Date'],y=df['NewConfirmed'],showlegend=False,text='NewConfirmed cases'),row=1, col=1)
            fig.add_trace(go.Bar(x=df['Date'],y=df['NewDeaths'],showlegend=False,text='NewDeaths'),row=1, col=2)
            fig.add_trace(go.Bar(x=df['Date'],y=df['Confirmed'],showlegend=False,text='Confirmed cases'),row=2, col=1)
            fig.add_trace(go.Bar(x=df['Date'],y=df['Deaths'],showlegend=False,text='Deaths'),row=2, col=2)          
            
            #fig.update_layout(height=500, width=800) # ,title_text="COVID-19 country statistic"
            fig.update_layout(margin={'l': 20, 'b': 10, 't': 50, 'r': 0}, hovermode='closest')
        return fig
    
        
if __name__ == '__main__': 
    app = dash.Dash(__name__)
    layer = layperOutClass(app)
    setupApp(layer,app)
    app.run_server(debug=True)
