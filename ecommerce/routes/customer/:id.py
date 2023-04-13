from __main__ import app

from mysql.connector.cursor import MySQLCursor

from ecommerce.api import database


@app.route('/customer/<int:customer_id>')
@database
def get_customer_by_id(cursor: MySQLCursor, customer_id: int):
    cursor.execute('SELECT * FROM customer WHERE id = %s', (customer_id,))
    return cursor.fetchone()
