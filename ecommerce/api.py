from flask import Flask

from utils.connection import get_database
from utils.load_routes import load_routes

app = Flask(__name__)

database = get_database('ecommerce_martinelli_alessandro')

if __name__ == '__main__':
    load_routes()
    app.run()
