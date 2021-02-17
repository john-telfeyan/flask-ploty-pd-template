# -*- coding: utf-8 -*-

from flask import render_template, url_for
from flask_app import flask_app
import pandas as pd
import plotly.figure_factory as ff
from plotly.offline import plot

import os

def loop_content():

    posts = [
        {
            'header': 'Post 1',
            'body': 'first content'
        },
        {
            'header': 'Post 2',
            'body': 'Second Content!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

def has_no_empty_params(rule):
    ''' helper function for site-map 
    '''
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@flask_app.route('/')
@flask_app.route('/index')
@flask_app.route("/site-map")
def site_map():
    '''
    https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app
    '''
    
    links = []
    for rule in flask_app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append({"url": url, "route": rule.endpoint})
     
    return render_template('site-map.html', title='Home', link_list=links)
    # links is now a list of url, endpoint tuples
    
@flask_app.route("/hello-table")
def hello_table():
    df = pd.read_csv("data/hello_world.csv")
    fig = ff.create_table(df)
    return plot(fig, output_type='div')
    