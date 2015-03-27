import plotly.plotly as py
import time
import sqlite3
import time
from flask import Flask, request, g, render_template, redirect
from plotly.graph_objs import *
import webbrowser
py.sign_in("Sunti","h7ov1pwg6p")
def handNumber(a):
    fingerNum=0
    for finger in hands:
        for letter in finger:
            if letter==a:
                return fingerNum
        fingerNum+=1
    return 9
amounts=[0,0,0,0,0,0,0,0,0,0]
finger0=['~','`','1','!','q','a','z']
finger1=['2', '@','w','s','x']
finger2=['3','#','e','d','c']
finger3=['4','5','%','$','t','g','b','r','f','v']
finger4=['6','7', '^','&','y','u','h','j','n','m']
finger5=['8','*','i','k',',','<']
finger6=['9','(','o','l','.','>']
finger7=['0',')','p','/','?',';',':','"','+','-','{','}',"'",'_','[',']']
finger8=[' ']
hands=[finger0,finger1,finger2,finger3,finger4,finger5,finger6,finger7,finger8]
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def typecounter():
    return render_template('index.html')

@app.route("/refresh", methods=["POST"])
def receive_type():
    def operate(inputVal):
        for a in inputVal.lower():
            amounts[handNumber(a)]+=1
        for i in range(10):
            print('Finger ',i,'was used: ',amounts[i],' times')
        data = Data([
            Bar(
                x=['LPinky','LRing','LMiddle','LIndex','RIndex','RMiddle','RRing','RPinky','Thumb','Unknown'],
                y=amounts
            )
        ])
        layout = Layout(
            title=inputVal,
            xaxis=XAxis(
                title='Finger',
                titlefont=Font(
                    family='Courier New, monospace',
                    size=12,
                    color='#7f7f7f'
                )
            ),
            yaxis=YAxis(
                title='Frequency',
                titlefont=Font(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
        fig = Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='fingerDistribution')
    print("44s")
    print(type(request.form["text"]))
    inputVal=request.form["text"]
    print(inputVal)
    operate(inputVal)
    return redirect('/#portfolio')

if __name__ == "__main__":
    app.run(debug='true')

def operate(inputVal):
    for a in inputVal.lower():
        amounts[handNumber(a)]+=1
    for i in range(10):
        print('Finger ',i,'was used: ',amounts[i],' times')
    data = Data([
        Bar(
            x=['LPinky','LRing','LMiddle','LIndex','RIndex','RMiddle','RRing','RPinky','Thumnb','Unknown'],
            y=amounts
        )
    ])
    layout = Layout(
        title='Text: '+inputVal,
        xaxis=XAxis(
            title='Finger',
            titlefont=Font(
                family='Courier New, monospace',
                size=12,
                color='#7f7f7f'
            )
        ),
        yaxis=YAxis(
            title='Frequency',
            titlefont=Font(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    plot_url = py.plot(data, filename='fingerDistribution')
    #output to https://plot.ly/~Sunti/3/
