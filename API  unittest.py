import unittest
import json
import warnings
from Final_Api import app


class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def index_page(self):
        response = self.app.get("/")
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
        response = self.app.get('/City')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))

    def get_City(self):
        response = self.app.get('/City/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))

    def City_by_id_not_found(self):
        response = self.app.get(f"/City/6969")
        self.assertEqual(response.status_code, 404) 

    def add_City(self):
        data = {
            "NAME": "Jhon Weak",
            "country_Code": "PH",
            "District": "Tondo"
        }
        response = self.app.post("/City", json=data)
        self.assertEqual(response.status_code, 201)

    def update_City(self):
        data = {
            "NAME": "Lebron",
            "country_Code": "USA",
            "District": "America"
    
        }
        response = self.app.put("/City/2", json=data)
        self.assertEqual(response.status_code, 201)

    
    def test_delete_customer(self):
        response = self.app.delete("/City/1000")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()