from flask import Flask, request,redirect
import mysql.connector


app = Flask(__name__)

def get_db_connection():
        return mysql.connector.connect(
        host="mysql",
        user="enas",
        password="enas226",
        database="college"
    )
    
@app.route('/')
def home():
    
    return '''
        
        
        <html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="Task">
        <h2 class="title">Add Student :</h2>
        <form action="/add" method="post">
            <p> Name: </p> 
            <input class="text" type="text" name="name"><br><br>
             <p> Email: </p> 
            <input class="text" type="email" name="email"><br><br>
            <input type="submit" class="add-btn" value="Add">
        </form>
        <hr>
        <a href="/users">Show Students</a>
        </div>
    </body>
    </html>
    '''
    
    
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/users')

@app.route('/users')
def show_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, email FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    html = "<h2>Students List</h2><ul>"
    for row in data:
        html += f"<li>{row[0]} - {row[1]}</li>"
    html += "</ul><a href='/'>Back</a>"

    return html

        

app.run(host='0.0.0.0', port=5000)
