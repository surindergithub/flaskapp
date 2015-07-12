from flaskapp import app
import test

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"


def mytestfunction():
   """docstring for mytestfunction"""
    dict = {'a': 'test', 'b': 'test2'}
    print('{1}'.format(dict))

