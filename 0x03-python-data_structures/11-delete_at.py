#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
     if 0 <= idx < len(my_list):
         result = my_list[:idx] + my_list[idx + 1:]
         return result
     else:
         return my_list
