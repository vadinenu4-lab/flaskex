from flask import Flask
app = Flask (__name__)
@app.route('/')
def hello():
    return "Hello"
@app.route ('/<name>')
def helloname(name):
    return "Hello "+name
app.run(debug=True)