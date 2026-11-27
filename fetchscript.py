from flask import Flask,render_template,request
app = Flask (__name__)
@app.route('/')
def registration():
    return render_template('fetch.html')

@app.route('/success',methods=['post'])
def printdata():
    result=request.form
    return render_template('resultfetch.html',result=result)

app.run(debug=True)