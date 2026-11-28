from flask import *
app = Flask (__name__)

@app.route('/') 
def upload():
    return render_template('file.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
         f=request.files['file']
         f.save(f.filename)
         return"success"
app.run(debug=True)