from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, send_file, session
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
mylist = []

app = Flask(__name__)

def calc(site):
   # site= "https://economictimes.indiatimes.com/hdfc-bank-ltd/stocks/companyid-9195.cms"
    a =[]
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('h1',attrs={'class':'company_name'}):
        company_name = fp.text.strip()
    for fp in soup.find_all('span',attrs={'class':'ltp'}):
        company_price = fp.text.strip()
        company_price = company_price.replace(',','')
        company_price=float(company_price)
        break
    for fp in soup.find_all('ul',attrs={'class':'metrics nse_tab'}):
        #print(fp)
        l=[]
        for x in fp.find_all('li'):
            l.append(x)
        for y in l[9].find_all('span',attrs={'class':'val'}):
            tmp_high = y.text.strip()
            high=""
            for i in tmp_high:
                if(i==','):
                    continue
                if(i=='/'):
                    break
                high+=i
            high=float(high)
            break
        break
    h_change = (high-company_price)/high
    h_change*=100
    a.append(company_name);a.append(company_price);a.append(high);a.append(round(h_change,2))
    mylist.append(a)

@app.route('/')
def index():
    site= "https://economictimes.indiatimes.com/indices/nifty_50_companies"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('div',attrs={'id':'ltp'}):
        nifty = fp.text.strip()
        nifty=float(nifty)
    for fp in soup.find_all('span',attrs={'id':'yearHigh'}):
        nifty_high = fp.text.strip()
    nifty_high=float(nifty_high)
    change_per = (nifty_high-nifty)/nifty_high
    change_per*=100
    change_per=round(change_per,2)
    mylist.clear()
    site= "https://economictimes.indiatimes.com/hdfc-bank-ltd/stocks/companyid-9195.cms"
    calc(site)
    site= "https://economictimes.indiatimes.com/tata-consultancy-services-ltd/stocks/companyid-8345.cms"
    calc(site)
    site= "https://economictimes.indiatimes.com/reliance-industries-ltd/stocks/companyid-13215.cms"
    calc(site)
    site= "https://economictimes.indiatimes.com/infosys-ltd/stocks/companyid-10960.cms"
    calc(site)
    site= "https://economictimes.indiatimes.com/housing-development-finance-corporation-ltd/stocks/companyid-13640.cms"
    calc(site)    
    site= "https://economictimes.indiatimes.com/hindustan-unilever-ltd/stocks/companyid-13616.cms"
    calc(site)
    site= "https://economictimes.indiatimes.com/hero-motocorp-ltd/stocks/companyid-13636.cms"
    calc(site)
    site= "https://economictimes.indiatimes.com/britannia-industries-ltd/stocks/companyid-13934.cms"
    calc(site)
    site = "https://economictimes.indiatimes.com/bajaj-auto-ltd/stocks/companyid-21430.cms"
    calc(site)
    site ="https://economictimes.indiatimes.com/ultratech-cement-ltd/stocks/companyid-3027.cms"
    calc(site)
    site ="https://economictimes.indiatimes.com/bajaj-finance-ltd/stocks/companyid-11260.cms"
    calc(site)
    site ="https://economictimes.indiatimes.com/asian-paints-ltd/stocks/companyid-14034.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/icici-bank-ltd/stocks/companyid-9194.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/acc-ltd/stocks/companyid-6.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/wipro-ltd/stocks/companyid-12799.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/larsen-toubro-ltd/stocks/companyid-13447.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/itc-ltd/stocks/companyid-13554.cms"
    calc(site)
    site = "https://economictimes.indiatimes.com/maruti-suzuki-india-ltd/stocks/companyid-11890.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/grasim-industries-ltd/stocks/companyid-13696.cms"
    calc(site)
    site="https://economictimes.indiatimes.com/state-bank-of-india/stocks/companyid-11984.cms"
    calc(site)
    print('done')
    return render_template('index.html',nifty=nifty,nifty_high=nifty_high,change_per=change_per,mylist=mylist)

if __name__ == "__main__":
    print('started')
    app.run(debug=True)