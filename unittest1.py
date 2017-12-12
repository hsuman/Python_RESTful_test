import unittest 
from genesys import app
from db import Users
from mongoengine import *

class MyTestClass(unittest.TestCase): 

  # initialization logic for the test suite declared in the test module
  # code that is executed before all tests in one test run
  @classmethod
  def setUpClass(cls):
       pass 

  # clean up logic for the test suite declared in the test module
  # code that is executed after all tests in one test run
  @classmethod
  def tearDownClass(cls):
       pass 

  # initialization logic
  # code that is executed before each test
  def setUp(self):
      self.client = app.test_client()
      #connect(host='mongodb://localhost:27017/testdb')
      #Users(Id=1,fname="2",lname="3",latitude="4",longitude="5").save()

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass 


  def test_users_status_code(self):
    result = self.client.get('/prt/api/v1.0/users') 
    self.assertEqual(result.status_code, 200)  

  def test_user_id_status_code(self):
    result = self.client.get('/prt/api/v1.0/users/1') 
    self.assertEqual(result.status_code, 200)

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()