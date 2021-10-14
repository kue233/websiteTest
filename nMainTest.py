from flask import Flask,render_template,redirect,session,make_response,jsonify,request
from GraphFunc import CreateGraph
import datetime
from dateutil.relativedelta import relativedelta
import os

app = Flask(__name__)
app.debug=True
app.config["SERVER_NAME"]='kue233.com:5000'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=31)

ticker_save = 'aa'
end_time = None
QQQ_LIST = 'AAPL MSFT AMZN GOOG FB GOOGL TSLA NVDA PYPL ADBE CMCSA INTC CSCO NFLX PEP AVGO TMUS TXN COST QCOM AMGN CHTR SBUX INTU AMAT ISRG AMD BKNG LRCX MDLZ MU ZM GILD ADP MRNA ATVI CSX FISV MELI ILMN ADI BIIB ADSK JD NXPI REGN ASML KHC BIDU VRTX IDXX KLAC MNST KDP DOCU ALGN WBA MAR EXC EBAY EA ROST AEP LULU PDD MCHP WDAY SNPS ALXN DXCM MTCH PAYX CTSH ORLY XEL CTAS CDNS MRVL NTES TEAM PCAR XLNX FAST CPRT PTON ANSS SWKS SGEN VRSK SIRI MXIM OKTA VRSN CERN CDW DLTR SPLK TCOM INCY CHKP FOXA FOX'
#QQQ_LIST = 'ZM'
"""
def bcList(l):
    x = l.split(' ')
    return x
"""
#LRCX MDLZ MU ZM

"""
this method is used to prevent the issue when transfer data to front end and then transfer back, it cannot contains space.
"""
def ReplaceSpace(str1):
    if str1 != None:
        g = str1.replace(',',' ')
        return g
    return None

@app.route("/index",methods=['GET','POST'])
def index():
    global ticker_save
    global end_time
    # if there is a value submitted to back end
    if request.method == 'POST':
        # get all values and data from front end
        ticker = request.form.get('ticker')
        ticker_save = ticker
        ticker_input = ReplaceSpace(ticker)
        if request.form.get('QQQ') == 'QQQ':
            ticker = QQQ_LIST
        start = request.form.get('start')
        end = request.form.get('end')
        end_time = end
        yValue = request.form.get('yValue')
        graphtype = request.form.get('graphtype')
        ticker_save = ticker
        
        # change end date in front end (format:str) to the format datetime to be able to process in back end
        end = datetime.datetime.strptime(end, '%Y-%m-%d')
        testword = ticker 
        timeitv = request.form.get('timeitv')
        
        # the values that transfer from time duration buttons in search bar
        if(timeitv == '3D'):
            CreateGraph().createGraphs(ticker_input,start=end+datetime.timedelta(days=-3),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=3)
        elif(timeitv == '1W'):
            CreateGraph().createGraphs(ticker_input,start=end+datetime.timedelta(days=-7),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=7)
        elif(timeitv == '1M'):
            CreateGraph().createGraphs(ticker_input,start=end-relativedelta(months=1),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=30)
        elif(timeitv == '3M'):
            CreateGraph().createGraphs(ticker_input,start=end-relativedelta(months=3),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=92)
        elif(timeitv == '6M'):
            CreateGraph().createGraphs(ticker_input,start=end-relativedelta(months=6),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=185)
        elif(timeitv == '1Y'):
            CreateGraph().createGraphs(ticker_input,start=end-relativedelta(years=1),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=365)
        elif(timeitv == '3Y'):
            CreateGraph().createGraphs(ticker_input,start=end-relativedelta(years=3),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=1035)
        elif(timeitv == '5Y'):
            CreateGraph().createGraphs(ticker_input,start=end-relativedelta(years=5),end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input,days=1825)
        else:
            CreateGraph().createGraphs(ticker_input,start=start,end=end,y_value=yValue,graph_type=graphtype)
            CreateGraph().yboxPlots(listEnter=ticker_input)
        return render_template('yfIndex_result_2.html',ticker=ticker_save, start=start,end=end,yValue = yValue, graphtype=graphtype,testword=testword)
    return render_template('yfIndex.html')


# create a route called intro
@app.route('/intro')
def intro():
    return render_template('intro.html')

# create a route called about
@app.route('/about')
def about():
    return render_template('about.html')

# create a route called contact, but it is used to display paper
@app.route('/contact')
def contact():
    return render_template('contact.html')

# run code
if __name__ =='__main__':
    app.run()   



