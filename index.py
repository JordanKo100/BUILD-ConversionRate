from flask import Flask, render_template, request
import json
from api import *

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    convertedPrice = 1.0
    TOcurrency = ''
    FROMcurrency = ''
    if request.method == 'POST': #Executes on-click 
        amount = request.form['amount'] #parses the amount inputted from user
        TOcurrency = request.form.get('to') #parses the currency user wants
        FROMcurrency = request.form.get('from') #parses the currency user wants to change from
        exchange_rates(float(amount),FROMcurrency,TOcurrency) #call api function to retrieve converted amount
        
        #extracts data from conversions.json file to retrieve new value of currency
        with open('conversions.json') as json_file:
            price_data = json.load(json_file)
            convertedPrice = price_data['conversion_result']
    
    #needed to list the different countries and their currencies in the .html file
    with open('exchange.json') as json_file:
        data = json.load(json_file)
        countryMap = data['conversion_rates']
        countries = countryMap.keys()
        
    return render_template('main.html', countries = countries, convertedPrice = convertedPrice, TOcurrency = TOcurrency,FROMcurrency = FROMcurrency)

if __name__ == "__main__":
    app.run(debug=True)