from __main__ import app

from mysql.connector.cursor import MySQLCursor

from ecommerce.api import database


@app.route('/customer/<int:customer_id>/orders')
@database
def get_customer_orders(cursor: MySQLCursor, customer_id: int):
    cursor.execute("SELECT * FROM request WHERE customerId=%s", (customer_id,))
    return cursor.fetchall()
