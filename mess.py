from flask import Flask,render_template
app = Flask (__name__)

@app.route('/')
def hello():
    dict={'maths':80,'programming':90,'digital':70}
    return render_template('message.html',result=dict)

@app.route ('/<uname>')
def helloname(uname):
    return render_template('message.html',name=uname)

app.run(debug=True)