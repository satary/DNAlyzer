from model import InputForm
from flask import Flask, render_template, request, json
import compute

app=Flask(__name__)

@app.route('/DNAlysis',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/query',methods=['POST'])
def query():
    print("query")
    if request.method=='POST' and form.validate():
        data = json.loads(request.data)
        return draw_fig(PDB_index)
    else:
        data=None

    

if __name__=='__main__':
    app.run(debug=True) 
