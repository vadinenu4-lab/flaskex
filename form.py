from flask import Flask,request
app = Flask (__name__)
@app.route('/formlogin',methods={'post'})
def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=="user" and password=="123":
         return "welcome %s"%uname
    else:
        return "try again"
app.run(debug=True)