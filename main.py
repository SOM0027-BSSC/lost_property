# Author: Caio Sommer , Mahdi Mobarak , Oscar Mason
# Date: 7-8-2025
from flask import Flask, render_template, request

items={}

app = Flask(__name__) 
#hello
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/find")
def find():
    return render_template('find.html')

@app.route("/find", methods=['POST'])
def find_item():
    print(request.form)

@app.route('/report', methods=['POST'])
def add_item():
    print(request.form)
    items[request.form['description']] = {
        "author": request.form['name'],
        "question": request.form['question'],
        "answer": request.form['answer']
    }
    return "Your item has been added. <br><a href='/'>Main Page</a>"

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)





# har har har har 🗿
#🧟🐔 ( ͡° ͜ʖ ͡°)
#wtf does this even mean?