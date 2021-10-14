from flask import Flask,render_template,redirect,session,make_response,jsonify,request
from GraphFunc import CreateGraph
import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
app.debug=True
app.config["SERVER_NAME"]='kue233.com:5000'


QQQ_LIST = 'AAPL MSFT AMZN GOOG FB GOOGL TSLA NVDA PYPL ADBE CMCSA INTC CSCO NFLX PEP AVGO TMUS TXN COST QCOM AMGN CHTR SBUX INTU AMAT ISRG AMD BKNG LRCX MDLZ MU ZM GILD ADP MRNA ATVI CSX FISV MELI ILMN ADI BIIB ADSK JD NXPI REGN ASML KHC BIDU VRTX IDXX KLAC MNST KDP DOCU ALGN WBA MAR EXC EBAY EA ROST AEP LULU PDD MCHP WDAY SNPS ALXN DXCM MTCH PAYX CTSH ORLY XEL CTAS CDNS MRVL NTES TEAM PCAR XLNX FAST CPRT PTON ANSS SWKS SGEN VRSK SIRI MXIM OKTA VRSN CERN CDW DLTR SPLK TCOM INCY CHKP FOXA FOX'
#QQQ_LIST = 'ZM'
"""
def bcList(l):
    x = l.split(' ')
    return x
"""
#LRCX MDLZ MU ZM

@app.route("/index",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        if request.form.get('QQQ') == 'QQQ':
            ticker = QQQ_LIST
        start = request.form.get('start')
        end = request.form.get('end')
        yValue = request.form.get('yValue')
        graphtype = request.form.get('graphtype')
        session['ticker'] = ticker
        """resp = make_response(render_template('yfindex_result.html'))
        resp.set_cookie('ticker', ticker)
        resp.set_cookie('start', start)
        resp.set_cookie('end', end)
        resp.set_cookie('yValue', yValue)
        resp.set_cookie('graphtype', graphtype)"""

        """
        paraDict = {
            'ticker':ticker,
            'start':start,
            'end':end,
            'yValue':yValue,
            'graphtype':graphtype}
            """
        #tickerList = bcList(ticker)
        #print(ticker,start,end,yValue,graphtype)
        end = datetime.datetime.strptime(end, '%Y-%m-%d')
        testword = session.get("ticker")
        timeitv = request.form.get('timeitv')
        """
        ticker = request.cookies.get('ticker')
        end=request.cookies.get('end')
        yValue = request.cookies.get('yValue')
        graphtype = request.cookies.get('graphtype')
        """
        if(timeitv == '3D'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end+datetime.timedelta(days=-3),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '1W'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end+datetime.timedelta(days=-7),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '1M'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end-relativedelta(months=1),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '3M'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end-relativedelta(months=3),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '6M'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end-relativedelta(months=6),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '1Y'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end-relativedelta(years=1),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '3Y'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end-relativedelta(years=3),end=end,y_value=yValue,graph_type=graphtype)
        elif(timeitv == '5Y'):
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=end-relativedelta(years=5),end=end,y_value=yValue,graph_type=graphtype)
        else:
            CreateGraph().createGraphs(user_input=session.get("ticker"),start=start,end=end,y_value=yValue,graph_type=graphtype)
        CreateGraph().yboxPlots(listEnter=ticker)
        return render_template('yfIndex_result.html',ticker=ticker, start=start,end=end,yValue = yValue, graphtype=graphtype,testword=testword)
    return render_template('yfIndex.html')



@app.route('/intro')
def intro():
    return render_template('intro.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

class Config(object):
    SECRET_KEY = "kue233"

app.config.from_object(Config())

if __name__ =='__main__':
    app.run()   



"""
        a = 0
        b = 0
        c = 0
        d = 0
        if start != None:
            a=1
        if end != None:
            b=2
        if yValue != None:
            c=4
        if graphtype != None:
            d=8
        #this func create graph in the light of whether entered the 4 parameter
        def switcherFunc(arugument):
            switcher = {
            0:CreateGraph().createGraphs(ticker), 
            1:CreateGraph().createGraphs(ticker,start=start),
            2:CreateGraph().createGraphs(ticker,end=end),
            3:CreateGraph().createGraphs(ticker,start=start,end=end),
            4:CreateGraph().createGraphs(ticker,y_value=yValue),
            5:CreateGraph().createGraphs(ticker,start=start,y_value=yValue),
            6:CreateGraph().createGraphs(ticker,end=end,y_value=yValue),
            7:CreateGraph().createGraphs(ticker,start=start,end=end,y_value=yValue),
            8:CreateGraph().createGraphs(ticker,graph_type=graphtype),
            9:CreateGraph().createGraphs(ticker,start=start,graph_type=graphtype),
            10:CreateGraph().createGraphs(ticker,end=end,graph_type=graphtype),
            11:CreateGraph().createGraphs(ticker,start=start,end=end,graph_type=graphtype),
            12:CreateGraph().createGraphs(ticker,y_value=yValue,graph_type=graphtype),
            13:CreateGraph().createGraphs(ticker,start=start,y_value=yValue,graph_type=graphtype),
            14:CreateGraph().createGraphs(ticker,end=end,y_value=yValue,graph_type=graphtype),
            15:CreateGraph().createGraphs(ticker,start=start,end=end,y_value=yValue,graph_type=graphtype)
            }
            return switcher[arugument]
        
        if ticker != None and ticker != '':
            #switcherFunc(a+b+c+d)
        else:
            return render_template('yfIndex.html',noTicker = 'please enter at least one ticker name. i.e: GOOG')
            """