from __main__ import app

from mysql.connector.cursor import MySQLCursor

from ecommerce.api import database
from utils.StatusCodeException import StatusCodeException


@app.route('/customer/<int:customer_id>')
@database
def get_customer_by_id(cursor: MySQLCursor, customer_id: int):
    cursor.execute('SELECT * FROM customer WHERE id = %s', (customer_id,))

    customer = cursor.fetchone()

    if customer is None:
        raise StatusCodeException('Customer not found', 404)

    return customer
