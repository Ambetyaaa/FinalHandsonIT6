from flask import Flask, Response, request, jsonify, make_response
from flask_mysqldb import MySQL

DB_App = Flask(__name__)
DB_App.config["MYSQL_HOST"] = "127.0.0.1"
DB_App.config["MYSQL_USER"] = "root"
DB_App.config["MYSQL_PASSWORD"] = "AMBET3639root"
DB_App.config["MYSQL_DB"] = "world_x"
DB_App.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(DB_App)

def fetch_data(query):
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

@DB_App.route("/")
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

@DB_App.route("/city", methods=["GET"])
def city():
    query = "SELECT ID, Name, CountryCode, District FROM city"
    data = fetch_data(query)
    return make_response(jsonify(data), 200)

@DB_App.route("/city/<int:ID>", methods=["GET"])
def getcityID(ID):
    query = f"SELECT ID, Name, CountryCode, District FROM city WHERE ID = {ID}"
    data = fetch_data(query)
    if not data:
        return jsonify(f"city {ID} does not exist")
    return make_response(jsonify(data), 200)

#Adding city
@DB_App.route("/city", methods=["POST"])
def city_add():
    city = request.get_json()
    query = f"""
        INSERT INTO city (Name, CountryCode, District)
        VALUES ('{city['Name']}', '{city['CountryCode']}', '{city['District']}')
    """
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    return make_response(jsonify("city added successfully"), 201)

#Updating city
@DB_App.route("/city/<int:ID>", methods=["PUT"])
def city_update(ID):
    city = request.get_json()
    query = f"""
        UPDATE city
        SET Name = '{city['Name']}', CountryCode = '{city['CountryCode']}',
            District = '{city['District']}'
        WHERE ID = {ID}
    """
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    return make_response(jsonify(f"city {ID} updated successfully"), 201)

#Deleting city
@DB_App.route("/city/<int:ID>", methods=["DELETE"])
def city_delete(ID):
    query = f"DELETE FROM city WHERE ID = {ID}"
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    return make_response(jsonify(f"city {ID} deleted successfully"), 200)

if __name__ == "__main__":
    DB_App.run(debug=True)