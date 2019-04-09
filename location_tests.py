import unittest
from location import *

class TestLab1(unittest.TestCase):


    #REPR METHOD TESTS
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("SLO", 35.3, 150)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, 150)")
        loc = Location("SLO", 23, 150)
        self.assertEqual(repr(loc),"Location('SLO', 23, 150)")
        loc = Location("notSLO", 23, 150)
        self.assertEqual(repr(loc),"Location('notSLO', 23, 150)")
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")
        loc = Location("anywhere", 20, 179)
        self.assertEqual(repr(loc),"Location('anywhere', 20, 179)")


    #EQ METHOD TESTS
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc,loc2)
    def test_eq_isclose(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.30000000000000001, -120.7)
        self.assertEqual(loc,loc2)
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7000000000000001)
        self.assertEqual(loc,loc2)
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.300000001, -120.7000000000000001)
        self.assertEqual(loc,loc2)
    def test_eq_isnotclose(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.71)
        self.assertNotEqual(loc,loc2)
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.31, -120.7)
        self.assertNotEqual(loc,loc2)
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.31, -120.71)
        self.assertNotEqual(loc,loc2)
    def test_eq_notequal_all_three(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("notSLO", 79, -156.7)
        self.assertNotEqual(loc,loc2)
    def test_eq_notequal_1_attribute(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -156.7) 
        self.assertNotEqual(loc,loc2)
        loc = Location("SLO", 25, -156.7)
        loc2 = Location("SLO", 35.3, -156.7) 
        self.assertNotEqual(loc,loc2)
        loc = Location("SLO", 20, 40)
        loc2 = Location("notSLO", 20, 40) 
        self.assertNotEqual(loc,loc2)
    def test_eq_notequal_2_attributes(self):
        loc = Location("SLO", 40, -120.7)
        loc2 = Location("SLO", 35.3, -156.7) 
        self.assertNotEqual(loc,loc2)
        loc = Location("Nowhere", 25, -156.7)
        loc2 = Location("SLO", 35.3, -156.7) 
        self.assertNotEqual(loc,loc2)
        loc = Location("SLO", 20, 150)
        loc2 = Location("notSLO", 20, 40) 
        self.assertNotEqual(loc,loc2) 

if __name__ == "__main__":
        unittest.main()
