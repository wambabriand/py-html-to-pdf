from flask import Flask 

app = Flask(__name__)

from apis.v1 import *