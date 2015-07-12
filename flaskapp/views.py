from flaskapp import app
import test

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/testpage')
def testpage():
    """docstring for testpage"""
    return "test page"
