#!/usr/bin/env python3

def happy_new_year():
    x=11
    while x >=1:
        print (x)
        if(x==1):
            print("Happy New Year!")
            break
        x-=1
    
  

def square_integers(int_list):
    int_list=[square*square for square in int_list]
    return int_list
  

def fizzbuzz():
    y =1
    while y <=100:
        if(y%5==0 and y%3==0):
            print("FizzBuzz")
     
        elif(y%3==0):
            print("Fizz")
        elif(y%5==0):
            print("Buzz")
       
        else:
            print(y)    
        y+=1            