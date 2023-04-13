from __main__ import app

from ecommerce.api import database


@app.route('/customer/<int:customer_id>')
@database
def get_customer_by_id(cursor, customer_id):
    cursor.execute('SELECT * FROM customer WHERE id = %s', (customer_id,))
    return cursor.fetchone()
