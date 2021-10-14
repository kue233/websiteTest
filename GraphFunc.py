import plotly.express as px
import plotly.graph_objects as go
import datetime
import pandas as pd
from pandas_datareader import data as pdr
import plotly.io as pio
import yfinance as yf

from dateutil.relativedelta import relativedelta

"""
this function is to create a graph with parameters: ticker name, y value, type, end date, start date
"""
class CreateGraph():
    # this function is to split a string with space into a list
    def makeList(self,str):
        if str.__contains__(" ") == False:
            return [str]
        
        else:
            return str.split()

    def percentChange(self,closing_prices, days=1):
        result = [0]
        closing_prices = closing_prices.iloc[::days]

        for x in range(len(closing_prices)-1):
            result.append((closing_prices[x] - closing_prices[x+1])/closing_prices[x])

        return result

    # this function is to create a box plot with parameter ticker and days
    def yboxPlots(self,listEnter, days=30):
        list = self.makeList(listEnter)
        dfs = []
        boxplotData = pd.DataFrame() 
        
        for x in list:
            df = yf.Ticker(x).history(period='max')
            #df = data.DataReader(x,'yahoo')
            arr = self.percentChange(df['Close'], days)
            df = df.iloc[::days]
            df['Percent Change'] = arr 
            dfs.append(df['Percent Change'])

        df = pd.concat(dfs, axis=1)
        df.columns = list

        for x in list:
            df['Tickers'] = x
            temp = df[[x,'Tickers']]
            temp.columns = ['Percent Change', 'Tickers']
            boxplotData = boxplotData.append(temp)

        fig = px.box(boxplotData, x = 'Tickers', y = 'Percent Change')
        fig.update_layout(template='plotly_dark')
        pio.write_html(fig, file='static/ticker/boxPlot.html', auto_open=False)

    def createGraphs(self,user_input, start=None, end=None, y_value='High', graph_type = 'Line'):
        title = ""
        tickers = self.makeList(user_input)

        #start = '' + start + '-1-1'
        #end = '' + end + '-12-31'


        if len(tickers) == 1:
            d = yf.Ticker(tickers[0]).history(start = start, end = end)

            if y_value == 'Percent Change':
                arr = self.percentChange(d['Close'])
                d['Percent Change'] = arr

            if graph_type == 'Line':
                fig = px.line(d, y=y_value, template = 'plotly_dark', hover_data=d.columns)

            else:
                fig = px.area(d, y=y_value, template = 'plotly_dark', hover_data=d.columns)




        else:
            if graph_type == 'Area':
                graph_type = 'tonexty'
            else:
                graph_type = None



            #create a list of databases 
            list = []
            for x in tickers:
                d = yf.Ticker(x).history(start = start, end = end)
                if y_value == 'Percent Change':
                    arr = self.percentChange(d['Close'])
                    d['Percent Change'] = arr
                list.append(d)


            #plot each database 1 by 1 
            fig = go.Figure()
            for x in range(len(list)):
                fig.add_trace(go.Scatter(x=list[x].index,y=list[x][y_value], name=tickers[x], fill=graph_type))

        #ending styling
        for x in range(len(tickers)): 
            if x != len(tickers)-1:
                title += (tickers[x] + " " + y_value + " vs ")
            else:
                title += (tickers[x] + " " + y_value) 

        fig.update_layout(title=title, title_x=0.5, template='plotly_dark')
        pio.write_html(fig, file='static/ticker/index.html', auto_open=False) 
        
#starttime = datetime.datetime(2016,1,1)
#endtime=datetime.datetime(2020,1,1)
#CreateGraph().createGraphs('AAPL',start=starttime,end=endtime,y_value='Low')
#CreateGraph().createGraphs('AAPL',start=datetime.datetime(2017,10,10),end=datetime.datetime(2018,10,23))
#print(CreateGraph().makeList(str='asdasd asd sdsd dddd'))

#end = datetime.datetime(2020,1,1)
#c =end - relativedelta(months=1)
#d = end - relativedelta(years=1)
#CreateGraph().createGraphs('AAPL',start=d,end=end,y_value='Low')