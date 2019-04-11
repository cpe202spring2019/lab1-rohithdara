
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return None
   maxval = int_list[0]
   for val in int_list:
      if val > maxval:
         maxval = val
   return maxval


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return []
   else:
      return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   if int_list[((high+low)//2)] == target:
      return (high+low)//2
   if low >= high:
      return None
   if target < int_list[((high+low)//2)]:
      return bin_search(target, low, ((high+low)//2)-1, int_list)
   if target > int_list[((high+low)//2)]:
      return bin_search(target,((high+low)//2)+1,high,int_list)
