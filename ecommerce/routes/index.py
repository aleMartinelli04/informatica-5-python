from __main__ import app


@app.route('/')
def index():
    return {'msg': 'Hello World!'}
