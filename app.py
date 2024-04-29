from flask import Flask, request, render_template
import csv
import mysql.connector


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        location = request.form['location']
        ngos = []
        with open('ngos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Location'].lower() == location.lower():
                    ngos.append(row)
        return render_template('results.html', ngos=ngos)
    else:
        return render_template('index1.html')

# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="donation_system_db"
)

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')


@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['desc']

        app.logger.info(f"Received form submission: Name={name}, Email={email}, Message={message}")

        cursor = db.cursor()
        sql = "INSERT INTO contact_us (name, email, message) VALUES (%s, %s, %s)"
        val = (name, email, message)
    
    try:
            cursor.execute(sql, val)
            db.commit()
            app.logger.info("Form data inserted successfully")
    except Exception as e:
            db.rollback()
            app.logger.error(f"Error inserting form data: {e}")
    finally:
            cursor.close()

    return "Form submitted successfully!"

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/submit_book_form', methods=['POST'])
def submit_book_form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        kind = request.form['kind']
        no = request.form['no']

        # Insert data into database
        cursor = db.cursor()
        sql = "INSERT INTO book_donation (name, email, phone, address, kind, no) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, email, phone, address, kind, no)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        return "Form submitted successfully!"


@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/submit_food_form', methods=['POST'])
def submit_food_form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        serve = request.form['serve']
        address = request.form['address']
        cook = request.form['cook']

        # Insert data into database
        cursor = db.cursor()
        sql = "INSERT INTO food (name, email, phone, serve, address, cook) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, email, phone, serve, address, cook)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        return "Form submitted successfully!"


@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/submit_clothes_form', methods=['POST'])
def submit_clothes_form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        age = request.form['age']
        no = request.form['no']

        # Insert data into database
        cursor = db.cursor()
        sql = "INSERT INTO clothes (name, email, phone, address, age, no) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, email, phone, address, age, no)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)


