#!C:\Python33\python.exe
#https://projecteuler.net/problem=31
       
def ways_to_make_change(amount, denom_list):

    def recursive_ways(amt, lst):
        if amt == 0: return 1
        if len(lst) == 1:
            if amt % lst[0] == 0:
                return 1
            else: return 0
        else:
            ways = 0
            lst_copy = lst
            while lst_copy and lst_copy[0] > amt:
                lst_copy.pop(0)
            denom = lst_copy[0]
            for times in range(0, amt + 1, denom):
                ways += recursive_ways(amt - times, lst_copy[1:])
            return ways

    if amount <= 0:
        return 0
    list_copy = denom_list[:]
    
    for denom in denom_list:
        if denom > amount:
            list_copy.remove(denom)
            
    list_copy.sort(key=lambda x: -x)
    
    return recursive_ways(amount, list_copy)
    
answer = ways_to_make_change(200, [200,100,50,20,10,5,2,1]) 

import clip
clip._and_print(answer)