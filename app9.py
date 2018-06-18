#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 23:09:43 2018

@author: kiyoumars
"""
import datetime
import quandl
#import pandas_datareader.data as web
#import pandas_datareader as pdr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Thick data:', validators=[validators.required()])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print(request.form.getlist('box'))
        listOfOptions=request.form.getlist('box')
        n=len(listOfOptions)
        start=datetime.datetime(2016,1,1)
        end=datetime.datetime(2018,1,1)
        stk = quandl.get("WIKI/" + name, start_date=start, end_date=end)

        color=["black","blue","red","green"]
     
        p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")

        for i in range(n):
            p1.line(stk.index,stk[listOfOptions[i]],color=color[i])
            
        show(p1) 

        script, div = components(p1)
 
        if form.validate():
      
            flash('Hey ' + name)
        else:
            flash('All the form fields are required. ')
 
    return render_template('a3.html', form=form)
 
if __name__ == "__main__":
    app.run()
