"""
Link: https://www.hackerrank.com/challenges/py-if-else/problem

=======================
           solution
=======================
"""

def main():
    x = int(input("Enter a number"))
    return odd_even(x)
    

def odd_even(n):
    if n % 2 != 0:
        print("Weird")
    if n % 2 == 0:
        if n in range(2, 6) or n > 20:
            print("Not Weird")
        else:
            print("Weird")
            
            
