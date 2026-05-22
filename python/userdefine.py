# the functions which aredefine by user based on there requirements are known as user define
#  function
#Syntax:-         def fname(arguments):     // it hve positional arguments
                #   <--1 tab--> program
                #   fname(arguments)      // it is actual arguments

# Example:-
"""def add():
    a= int(input('enter the first number :- '))
    b= int(input('enter the second number :- '))
    print(a+b)
add()"""

#  TYPE OF USER DEFINE FUNCTION:-
# 1) FUNCTION WITHOUT ARGUMENT AND WITHOUT RETURN VALUE:-  the function which is not take any argument 
# and also not return any value is known as function without argument and without return value

# 2) FUNCTION WITH ARGUMENT AND WITHOUT RETURN VALUE:- 
# 3) FUNCTION WITHOUT ARGUMENT AND WITH RETURN VALUE:-
# 4) FUNCTION WITH ARGUMENT AND WITH RETURN VALUE:-

# NOTE:- pass the argument and return value is not mandatory


# def:- it is the keyword that defines/create a function

# to execute the function,we have to call the fuction
# return keyword is use to stop the execution
# 



#&&&&&&&&&&&&&&&&&&&&&&& 1) FUNCTION WITHOUT ARGUMENT AND WITHOUT RETURN VALUE &&&&&&&&&&&&&&&&&&&&
#syntax:- 
# def fname():
# <-1Tab-> SB
# fname()


# def uppercase():
#     a= input('enter thr string:- ')
#     b= a.upper()
#     print(b)
# uppercase()

def add():
    a= int(input('enter the number:- '))
    b= int(input('enter the number:- '))
    return a+b
print(add())

