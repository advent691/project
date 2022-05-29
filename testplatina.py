from flask import Flask, render_template, request, session, redirect,url_for
import os
from pyowm import OWM
from pyowm.utils.config import get_default_config
import requests
from bs4 import BeautifulSoup as bs

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('8b425ee664dec0056763d897438d0299', config_dict)
folder = os.getcwd()
app = Flask(__name__, template_folder=folder)
app.secret_key=b'sadadadkglkalkflkafmkas'



@app.route('/',methods=["GET", 'POST'])
def index2():
    URL_TEMPLATE = "https://www.audit-it.ru/currency/"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    Doll = soup.findAll('a', class_='value value_green')
    x=0
    for quote in Doll:
        if x==0:
            doll= quote.text
        
    return render_template('templatess/page2.html',doll=doll) 

@app.route('/p3',methods=["GET", 'POST'])
def index3():
    
    #pogoda
    pogoda = request.args.get('pogoda')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(pogoda)
    w = observation.weather
    t = w.temperature("celsius")
    t1 = t['temp']
    return render_template('templatess/page3.html',t1=t1, pogoda=pogoda)
    
"""@app.route('/p3')
def index4():
        
    return render_template('templatess/page2.html') 
"""
if __name__ == "__main__":
    app.run()
    
