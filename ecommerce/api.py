from flask import Flask

from utils.connection import open_connection
from utils.load_routes import load_routes

app = Flask(__name__)

database = open_connection('ecommerce_martinelli_alessandro')

if __name__ == '__main__':
    load_routes()
    app.run()
