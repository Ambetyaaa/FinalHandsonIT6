from flask import Flask, Response, request, jsonify, make_response
from flask_mysqldb import MySQL

flask_app = Flask(__name__)
flask_app.config["MYSQL_HOST"] = "127.0.0.1"
flask_app.config["MYSQL_USER"] = "root"
flask_app.config["MYSQL_PASSWORD"] = "AMBET3639root"
flask_app.config["MYSQL_DB"] = "world_x"
flask_app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(flask_app)

def fetch_data(query):
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

@flask_app.route("/")
def homepage():
    return Response("""
    
            C.R.U.D  TABLE
    Creat . Retreive . Update . Delete
 
    SELECTION:
    1. ADD CITY TABLE
    2. RETRIEVE CITY TABLE
    3. UPDATE CITY TABLE
    4. DELETE CITY TABLE
    5. EXIT
    """, mimetype="text/plain")


