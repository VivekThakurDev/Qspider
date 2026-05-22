"""

def person(name,age):
    print(f"Name is {name},age is {age}")

person('Majnu',15)
person('Harapari',16)
"""
# packing :- storing multiple value into a single container is called packing ,
# Unpacking :- Extacing multiple value from single container is called unpacking 

# by using *arg and **karg we can perform packing and unpacking 

# type of packing 
# 1) single packing (*arg)
# 2) multiple packing (**kargs)
'''
Note:- * is a special charecter which is used for packing and unpacking
'''
"""
# Example
first, others,*last= 1,2,3,4,5
print(first)
print(others)
print(last)

"""

"""
def all_val(*args):
    print(args)

all_val(1,2,3,4,5)   
"""

## Unpacking    
"""
a,b,c=[10,20,30]

print(a)
print(b)
print(c)

"""
"""
a,*val,b=[1,2,3,4,5,67,8,9]
print(a)
print(val)
print(b)"""
"""

def my_fun(a,b,c,d):
    print(a+b+c+d)

list1=[10,20,30,40]
my_fun(*list1)
"""
"""

def student (name,roll,standard):
    print(f"Name is {name},Roll no is {roll},Class is {standard}")

s1= {'name':'Ravi','roll':21, 'standard':2}
student(**s1)"""



# Scope of variable 
"""
it define how far we acess a variable it follow "LEGB"

L=local
E= Enclosed/non=local
G= Global
B= Built in

L<E<G<B
"""

#--------------
# Global Scope
#--------------
# when it is declear in the global level then it is called GLobal Scope

#we can access it in :- Main Space, non local space(Enclosed space) and in the local space 
#

#-----------------
# Local Scope 
#-----------------
# when a variable inside the function then it is known as local scope variable
# we can acces the local variable inside local space only 
# Example
"""
a=10 #  Global scope
def wapper():
    b=50
    print(b) # local scope 
wapper() 
"""

#---------------
#Enclosed /Non local scope
#---------------
#the most function then inner must function must content local space  the outter function 
#    space is known as  enclosed scope or non-local scope
"""a=10 #global Scope 
def wapper():
    b=50 # Non local scope/Enclosed
    def inner ():
        c=100    
        print(c)  # Local Scope 
    inner()
wapper()
"""
#--------------
# Builtin Scope
#--------------
# it is a predefine scope which can be access in any python module 

#  Example of global 
"""
a = 10
def fun ():
    global a
    a+=5
    print(a)
fun()
"""

# Example of enclosed/non local
"""
def main():
    x = 10   # Enclosed / non local
    def inner():
        nonlocal x
        print(x)
        x-=5
        print('After modification :' ,x)
    inner()
main()"""


# What is the use of global keyword and nonlocal keyword
