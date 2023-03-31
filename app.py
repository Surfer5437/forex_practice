from xml.dom.minidom import Element
from flask import Flask, render_template, request, session
app=Flask(__name__)
import requests


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods=['POST'])
def home_post():
    convert_from=request.form['converting_from']
    convert_to=request.form['converting_to']
    from forex_python.converter import CurrencyCodes
    c = CurrencyCodes()
    print(c)
    list_of_currencies=[]
    for key in c:
        list_of_currencies.append(key['cc'])
        print('list should be list' +list_of_currencies)
    if convert_from in list_of_currencies:
        amount=request.form['amount']
        if amount != '':

            url = 'https://api.exchangerate.host/convert'
            response = requests.get(url, params={'from':convert_from,'to':convert_to,'amount':amount})
            data = response.json()
            info=data['info']['rate']
            total_converted=float(info) * float(amount)
            return render_template('home.html',info=total_converted)
    else:
        return '<h1>hi</h1>'





# def show_responce_in_dom():
    
# @app.route('/test')
# def test():
    
    # m=(cc,symbol,name)=c.__currency_data
    # print(m)