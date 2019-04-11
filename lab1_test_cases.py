import unittest
from lab1 import *

class TestLab1(unittest.TestCase):


    #MAX OF LIST ITERATIVE TESTS
    def test_max_list_iter_error(self):
    #Tests the error if the input list is None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter_empty(self):
    #Tests if the list is empty
        self.assertEqual(max_list_iter([]),None)
    def test_max_list_iter_odd(self):
    #Tests if the # of items in the list is odd
        self.assertEqual(max_list_iter([1,2,3,4,5,6,28,7,5]),28)
    def test_max_list_iter_even(self):
    #Tests if the #of items in the list is even
        self.assertEqual(max_list_iter([1,2,3,4,28,6,8,24]),28)
    def test_max_list_iter_same_number(self):
    #Tests is all the numbers in the list are the same
        self.assertEqual(max_list_iter([0,0,0,0,0,0,0,0]),0)
    def test_max_list_iter_first(self):
    #Tests if the max value is the first value
        self.assertEqual(max_list_iter([25,2,5,18,18,20]),25)
    def test_max_list_iter_last(self):
    #Tests if the max value is the last value
        self.assertEqual(max_list_iter([20,18,18,5,2,25]),25)



    #LIST REVERSAL TESTS
    def test_reverse_rec_odd(self):
    #Tests if the # of items in the list is odd
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    def test_reverse_rec_same_number(self):
    #Tests if all the items are the same
        self.assertEqual(reverse_rec([0,0,0,0,0]),[0,0,0,0,0])
    def test_reverse_rec_error(self):
    #Tests the error if the input list is None
        with self.assertRaises(ValueError):
            reverse_rec(None)
    def test_reverse_rec_empty(self):
    #Tests if the list is empty
        self.assertEqual(reverse_rec([]),[])
    def test_reverse_rec_single(self):
    #Tests if the list only has 1 item
        self.assertEqual(reverse_rec([1]),[1])
    def test_reverse_rec_even(self):
    #Tests if the list has an even # of items
        self.assertEqual(reverse_rec([1,2]),[2,1])
        self.assertEqual(reverse_rec([1,5,4,3]),[3,4,5,1])




    #BINARY SEARCH TESTS
    def test_bin_search_middle_target(self):
    #Tests if the target is in the middle
        list_val = [1,2,3,4,6,7,8]
        self.assertEqual(bin_search(4,0,len(list_val)-1, list_val), 3)
    def test_bin_search_odd(self):
    #Tests if the list has an odd # of items
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
    def test_bin_search_even(self):
    #Tests is the list has an even # of items
        list_val =[0,1,2,3,4,7,8,9,10,11]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
    def test_bin_search_odd_error(self):
    #Tests the error if the input list is None
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(4,0,25,list_val) 
    def test_bin_search_even_missing(self):
    #Tests if the target is not in the input list w/ an even # of items
        list_val = [1,2,3,4,6,7,8,9]
        self.assertEqual(bin_search(5,0,len(list_val)-1, list_val), None)
    def test_bin_search_odd_missing(self):
    #Tests if the target is not in the input list w/ an odd # of items
        list_val = [1,2,3,4,6,7,8]
        self.assertEqual(bin_search(5,0,len(list_val)-1, list_val), None)
    def test_bin_search_same_number(self):
    #Tests if the items in the list are all the same
        list_val = [1,1,1,1,1,1]
        self.assertEqual(bin_search(1,0,len(list_val)-1, list_val),2)
    def test_bin_search_high_equal_low(self):
    #Tests if there is only 1 item in the list (high will equal low)
        list_val = [1]
        self.assertEqual(bin_search(2,0,len(list_val)-1, list_val), None)
        list_val = [2]
        self.assertEqual(bin_search(2,0,len(list_val)-1, list_val),0)
    def test_bin_search_high_greater_low(self):
        list_val = [1,2,3,4,6,7,8,9]
        self.assertEqual(bin_search(9,5,2, list_val), None)
    def test_bin_search_high_minus_low(self):
    #Tests if there are only 2 items in the list (high-low = 1)
        list_val = [1,2]
        self.assertEqual(bin_search(1,0,len(list_val)-1,list_val),0)
        list_val = [1,2]
        self.assertEqual(bin_search(3,0,len(list_val)-1,list_val),None)
    def test_bin_search_end(self):
        list_val = [1,2,3,4,6,7,8,9]
        self.assertEqual(bin_search(9,0,len(list_val)-1, list_val), 7)




if __name__ == "__main__":
        unittest.main()

    
