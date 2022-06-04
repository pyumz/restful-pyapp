from flask import Flask
#from app import database

app = Flask(__name__)

from app import routes, errors, games
