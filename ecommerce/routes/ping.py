from __main__ import app


@app.route('/ping')
def ping():
    return {'ping': 'pong'}
