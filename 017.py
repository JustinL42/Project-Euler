#!C:\Python33\python.exe
#https://projecteuler.net/problem=17

under_ten_count = len('onetwothreefourfivesixseveneightnine')

upto_ten_count = len('ten') + under_ten_count

under_one_hundred_count = upto_ten_count + 8*under_ten_count + len('eleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen') + 10*len('twentythirtyfortyfiftysixtyseventyeightyninety')


upto_one_thousand_count =  under_ten_count*100 + 900*len('hundred') + 891*len('and') + 10*under_one_hundred_count + len('onethousand')




answer = upto_one_thousand_count

print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
