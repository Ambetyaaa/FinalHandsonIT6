import unittest
import json
import warnings
from Final_Api import DB_App


class MyDB_AppTests(unittest.TestCase):
    def setUp(self):
        DB_App.config["TESTING"] = True
        self.DB_App = DB_App.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def index_page(self):
        response = self.DB_App.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(),
     """
       
              C.R.U.D  TABLE
    Creat . Retreive . Update . Delete
 
    SELECTION:
    1. ADD CITY TABLE
    2. RETRIEVE CITY TABLE
    3. UPDATE CITY TABLE
    4. DELETE CITY TABLE
    5. EXIT

    """)
    #get functions

    def get_City(self):
        response = self.DB_App.get('/city')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))

    def get_City(self):
        response = self.DB_App.get('/city/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))

    def City_by_id_not_found(self):
        response = self.DB_App.get(f"/city/6969")
        self.assertEqual(response.status_code, 404) 

    def add_City(self):
        data = {
            "NAME": "Jhon Weak",
            "country_Code": "PH",
            "District": "Tondo"
        }
        response = self.DB_App.post("/city", json=data)
        self.assertEqual(response.status_code, 201)

    def update_City(self):
        data = {
            "NAME": "Lebron",
            "country_Code": "USA",
            "District": "America"
    
        }
        response = self.DB_App.put("/city/2", json=data)
        self.assertEqual(response.status_code, 201)

    
    def test_delete_customer(self):
        response = self.DB_App.delete("/city/501")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()