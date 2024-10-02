from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

# Customer data CSV file
DATA_FILE = 'akdata.csv'

# Simulated login credentials for developer
DEVELOPER_USERNAME = 'akshay'
DEVELOPER_PASSWORD = '193'

# Route for serving the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route for booking
@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']

    # Save customer data to CSV
    with open(DATA_FILE, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, email, gender])

    return jsonify(success=True)

# Route for developer login
@app.route('/developer-login', methods=['POST'])
def developer_login():
    username = request.form['username']
    password = request.form['password']

    if username == DEVELOPER_USERNAME and password == DEVELOPER_PASSWORD:
        return jsonify(success=True)
    else:
        return jsonify(success=False)

# Route for fetching customer data
@app.route('/get-customers')
def get_customers():
    customers = []
    try:
        with open(DATA_FILE, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                customers.append({'name': row[0], 'email': row[1], 'gender': row[2]})
    except FileNotFoundError:
        pass

    return jsonify(customers)

# Route for deleting all customer data
@app.route('/delete-all-customers', methods=['POST'])
def delete_all_customers():
    open(DATA_FILE, 'w').close()  # Clear the CSV file
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
