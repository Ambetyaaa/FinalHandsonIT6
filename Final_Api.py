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

@flask_app.route("/city", methods=["GET"])
def city():
    query = "SELECT ID, Name, CountryCode, District FROM city"
    data = fetch_data(query)
    return make_response(jsonify(data), 200)

@flask_app.route("/city/<int:ID>", methods=["GET"])
def getcityID(ID):
    query = f"SELECT ID, Name, CountryCode, District FROM city WHERE ID = {ID}"
    data = fetch_data(query)
    if not data:
        return jsonify(f"city {ID} does not exist")
    return make_response(jsonify(data), 200)

#adding city
@flask_app.route("/city", methods=["POST"])
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

#updating city
@flask_app.route("/city/<int:ID>", methods=["PUT"])
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

#deleting city
@flask_app.route("/city/<int:ID>", methods=["DELETE"])
def city_delete(ID):
    query = f"DELETE FROM city WHERE ID = {ID}"
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    return make_response(jsonify(f"city {ID} deleted successfully"), 200)

if __name__ == "__main__":
    flask_app.run(debug=True)