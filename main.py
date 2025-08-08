# Author: Caio Sommer (-10%), Mahdi Mobarak (-90%), Oscar Mason(200%)
# Date: 7-8-1984
from flask import Flask, render_template, request

items = []

app = Flask(__name__) 
#hello
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find')
def find():
    return render_template('find.html')

@app.route('/report', methods=['POST'])
def add_item():
    print(request.form)
    items.append({
        "author": request.form['name'],
        "description": request.form['description'],
        "question": request.form['question'],
        "answer": request.form['answer']
    })
    return "Your item has beeen<a href='/'>"

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)





# har har har har 🗿
#🧟🐔 ( ͡° ͜ʖ ͡°)
#wtf does this even mean?