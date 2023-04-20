import flask
from flask import Response
from mysql.connector import connect, MySQLConnection

from utils.StatusCodeException import StatusCodeException


def get_connection(db_name: str, user: str = 'root', password: str = '', host: str = 'localhost',
                   unix_socket: str = '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                   raise_on_warnings: bool = True) -> MySQLConnection:
    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': db_name,
        'unix_socket': unix_socket,
        'raise_on_warnings': raise_on_warnings
    }

    return connect(**config)


def open_connection(db_name: str, dictionary: bool = True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            connection = get_connection(db_name)
            cursor = connection.cursor(dictionary=dictionary)

            kwargs['cursor'] = cursor

            try:
                result = flask.jsonify(func(*args, **kwargs))

            except StatusCodeException as e:
                result = Response(e.message, e.code)

            cursor.close()
            connection.close()

            return result

        wrapper.__name__ = func.__name__

        return wrapper

    return decorator
