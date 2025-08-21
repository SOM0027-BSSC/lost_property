# Author: Caio Sommer , Mahdi Mobarak , Oscar Mason
# Date: 14-8-2025
from flask import Flask, render_template, request

items = {}
finders = {}

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', password="lost", itemslist=list(items.keys()), finderslist=list(finders.keys()), items=items, finders=finders)

@app.route("/find")
def find():
    print(items)
    return render_template('find.html', items=list(items.keys()))

@app.route("/find", methods=['POST'])
def find_item():
    finders[request.form["item"]] = {
        "name": items[request.form["item"]]["name"],
        "colour": request.form["colour"]
    }
    return "You request has been submitted. You will be emailed shortly if the details match up. <br><a href='/'>Return to main page</a>"

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/report', methods=['POST'])
def add_item():
    global items
    items[request.form["item"]] = {
        "name": request.form["name"],
        "colour": request.form["colour"]
    }
    return "Your item has been added. <br><a href='/'>Return to main page</a>"

if __name__ == '__main__':
    app.run(debug=True)