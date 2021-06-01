import pymongo
from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, send_file, session
from flask_cors import CORS, cross_origin
from bson.json_util import dumps
import json
app = Flask(__name__)
from update_route import *
mongo = pymongo.MongoClient(host="localhost",port=27017)
db=mongo.algoinvstr

@app.route('/')
def index():
    niftyv = db.nifty.find()
    companylist = db.toptwenty.find()
    return render_template('index.html',nifty=niftyv[0]["cur_val"],nifty_high=niftyv[0]["all_time_high"],change_per=niftyv[0]["down_per"],mylist=companylist,time=niftyv[0]["time"],date=niftyv[0]["date"])

@app.route('/update')
def call():
    updatecalled()
    niftyv = db.nifty.find()
    companylist = db.toptwenty.find()
    return render_template('index.html',nifty=niftyv[0]["cur_val"],nifty_high=niftyv[0]["all_time_high"],change_per=niftyv[0]["down_per"],mylist=companylist,time=niftyv[0]["time"],date=niftyv[0]["date"])


if __name__ == "__main__":
    print('started')
    app.run(debug=True)