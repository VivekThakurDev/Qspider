#-----------------
#polymorphism
#-----------------

'''
-> it is a phenomina where a single identity  different behavior  as per the context or situation 
-> in  this due to same name of method the last one override the first one.


'''

# Example ():
"""
def sum(a,b,c):
    print(a+b+c) 
temp=sum

def sum(a,b):
    print(a+b)

sum(2,4)
temp(2,3,5)

"""
'''
We have three type of polymorphism:
1) Method Overloading
2) Method Overiding
3) operator overloading

'''
#-------------------------
# Method Overloading
#-------------------------
"""
-> it is a type of polymorphism  where  method behave different by staying a single class 
-> In this function also behave different as per the requirement by overloading the extanceing method
"""
"""class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print('rec',a*b)

        elif a!=None:
            print('sqr',a*a)

        else:
            print('nothing')

obj1=Area()
obj1.find_area()
obj1.find_area(5)
obj1.find_area(6,5) 
"""

#-------------------------
# Method Overiding
#-------------------------
"""
-> it is a phenomia where due to same method/function name  the last method name override the first method  
-> 
"""
"""
class A :
    def show_msg(self):
        print('Good Morning')

class B(A):
    def show_msg(self):
        print('bye')

obj1=B()
obj2=A()
obj2.show_msg()
obj1.show_msg()

"""
#-------------------------
# Operator Overloading
#-------------------------
'''
-> it is ia phenomeno where we make opps to understand mathemeatical by using magic method 
# Magic Method :- these are the method which are workable on opps to understand the property of a operator 
'''

# WAP to create a calculator using magic method 

class calculator:
    def __init__(self,a):
        self.a=a

    def __add__(self, other):
        return self.a+other.a
    
    def __sub__(self,x):
        return self.a-x.a
    
    def __mul__(self, b):
        return self.a*b.a
    
ob1=calculator(12)
obj2=calculator(10)
print(ob1+obj2)
print(ob1-obj2)
print(ob1*obj2)