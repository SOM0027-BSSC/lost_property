# Author: Caio Sommer , Mahdi Mobarak , Oscar Mason
# Date: 21-8-2025
from flask import Flask, render_template, request, jsonify

items = {}
finders = {}
chosen_password = input("Enter the password for the dashboard: ")
print("Password is: "+chosen_password)
print("Go to 127.0.0.1/dashboard to view and manage requests.")

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    filtered_items = items.copy()
    filtered_finders = {k: v for k, v in finders.items() if k in filtered_items}
    
    return render_template('dashboard.html', password=chosen_password, items=filtered_items, finders=filtered_finders)


@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    item_key = data["item"]
    if item_key in items:
        del items[item_key]
        return jsonify({"status": "success", "message": "Item has been deleted."})
    else:
        return jsonify({"status": "error", "message": "Item not found."}), 404

@app.route("/find")
def find():
    print(items)
    return render_template('find.html', items=list(items.keys()))

@app.route("/find", methods=['POST'])
def find_item():
    finders[request.form["item"]] = {
        "original_name": items[request.form["item"]]["name"],
        "colour": request.form["colour"],
        "finder_name": request.form["finder"]
    }
    return "Your request has been submitted. You will be emailed shortly if the details match up. <br><a href='/'>Return to main page</a>"

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