from flask import *
app = Flask (__name__)
app.secret_key="login"
@app.route('/') 
def home():
    return render_template('f.html')

@app.route('/flogin',methods=['post'])
def login():
    error=None
    uname=request.form['uname']
    password=request.form['pass']
    if uname=="Nenu" and password=="123":
         flash("you are successfull login")
         return render_template('msg.html',name=uname)
    else:
        error="invalid username or password"
        return render_template('f.html',error=error)
        #abort(401)
        #return"try again"
        #return redirect(url_for("home"))
    
app.run(debug=True)