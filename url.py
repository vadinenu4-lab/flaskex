from flask import Flask,redirect,url_for
app = Flask (__name__)
@app.route('/')
def wc():
    return "welcome to python"
@app.route('/student')
def student():
    return "Hello,welcome students"
@app.route('/faculty')
def faculty():
    return "Hello,welcome faculty"
@app.route('/user/<name>')
def user(name):
    if name=='student':
        return redirect(url_for('student'))
    if name=='faculty':
        return redirect(url_for('faculty'))
app.run(debug=True)