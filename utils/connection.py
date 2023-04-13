import flask
from mysql.connector import connect, MySQLConnection


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

            result = func(*args, **kwargs)

            cursor.close()
            connection.close()

            return flask.jsonify(result)

        return wrapper

    return decorator
