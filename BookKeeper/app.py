from flask import Flask, request, jsonify, render_template
import mysql.connector
import webbrowser

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/edit')
def edit_page():
    return render_template('edit.html')

@app.route('/values', methods=["POST"])
def update_values():
    pathivuEn = request.form.get('pathivuEn')
    MNNo = request.form.get('pagupuEn')
    title = request.form.get('title')
    author = request.form.get('author')
    rate = request.form.get('rate')
    year = request.form.get('year')
    rackNo = request.form.get('rackNo')
    rackSide = request.form.get('rackSide')
    rowNo = request.form.get('rowNo')
    message = "files have uploaded sucessfully"
    
    # Dummy for checking the values are got from the front end 
    print(title)
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="libcheck3"
    )
    mycursor = mydb.cursor()
    mycursor.execute("""
CREATE TABLE IF NOT EXISTS mytable (
     SNO int AUTO_INCREMENT PRIMARY KEY,
     pathivuEn varchar(200),
     MNNo varchar(200),
     title varchar(200),
     author varchar(200),
     rate varchar(200),
     year varchar(200),
     rackNo varchar(200),
     rackSide varchar(200),
     rowNo varchar(200)
)
""")
    s = "INSERT INTO mytable (pathivuEn, MNNo, title, author, rate, year, rackNo, rackSide, rowNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(s, (pathivuEn, MNNo, title, author, rate, year, rackNo, rackSide, rowNo))
    mydb.commit()
    return jsonify({"message": message})

@app.route('/search', methods=["POST"])
def search():
    data = request.json
    search_input = data.get('search')
    print(f"Search input received: {search_input}")
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="libcheck3"
    )
    mycursor = mydb.cursor()
    query = "SELECT * FROM mytable WHERE SNO=%s"
    mycursor.execute(query, (search_input,))
    db = mycursor.fetchall()
    for d in db:
        print(d)
    return jsonify({'message': "nan vanduthuten", "data": db})

@app.route('/update', methods=["POST"])
def update():
    data = request.json
    SNO = data.get('regNo')
    pathivuEn = data.get('pathivuEn')
    MNNo = data.get('pagupuEn')
    title = data.get('title')
    author = data.get('author')
    rate = data.get('rate')
    year = data.get('year')
    rackNo = data.get('rackNo')
    rackSide = data.get('rackSide')
    rowNo = data.get('rowNo')

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="libcheck3"
        )
        mycursor = mydb.cursor()
        query = """
        UPDATE mytable 
        SET pathivuEn=%s, MNNo=%s, title=%s, author=%s, rate=%s, year=%s, rackNo=%s, rackSide=%s, rowNo=%s
        WHERE SNO=%s
        """
        mycursor.execute(query, (pathivuEn, MNNo, title, author, rate, year, rackNo, rackSide, rowNo, SNO))
        mydb.commit()
        return jsonify({"message": "Update successful"})
    
    except mysql.connector.Error as err:
        error_message = f"MySQL Error: {err.msg}"
        return jsonify({"message": error_message}), 400  # Return HTTP 400 Bad Request with error message

    finally:
        mycursor.close()
        mydb.close()

if __name__ == '__main__':
    app.run(debug=True)


