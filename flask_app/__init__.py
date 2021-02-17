# -*- coding: utf-8 -*-


from flask import Flask
from flask_bootstrap import Bootstrap


flask_app = Flask(__name__)


bootstrap = Bootstrap(flask_app)

from flask_app import routes #, models, errors