#-----------------------
# Multiple Inheritance
#-----------------------
'''

-> It is a type of inheritance where child class deviate it properties to more than one parent class is called multiple inheritance
-> It is a horizontal directional model


-> it is a model where multiple parent devate there properties to single child class 
-> It python this model is hypothetical in nature but t smetime it work due to dynamic nature of python

'''
# Syntax:-

'''
class A:
    ----
    |SB|
    ----
class B:
    ----
    |SB|
    ----
Classs C:
  -----
  |SB |
  ------

class D(A,B,C):
    ------
    | SB|
    ------


'''
# Example:-
"""class A:
    a=10
class B:
    pass
class C:
    z=100
    def __init__(self,a):
        self.a=a
class D(A,B,C):
    y='hello'

print(A.a,C.z)
print(D.a,D.z)"""


#  WAP to 
"""
class bat:
    length="3ft"
    weight='3kg'
    bellow='kashmiri'


class ball:
    ball_type='dues'
    brand='hf'
    color='Red'

class cricket(bat,ball):
    player="11 player"
    petchlength='5meter'
    def __init__(self,length,weight,bellow,ball_type,brand,color):
         self.length=length
         self.weight=weight
         self.bellow=bellow
         self.ball_type=ball_type
         self.brand=brand
         self.color=color

    def display(self):
        print(self.length,self.weight,self.bellow,self.ball_type,self.brand,self.color)
    
print(cricket.brand)


"""

#-------------------------
# herirical inheritance
#--------------------------


# it is a type of inheritance where single parent deviate there properties to multiple child class 
#

# Syntax:-
"""
class A:
    ----
    |SB|
    ----
class B(A):
    ----
    |SB|
    ----
Classs C(A):
  -----
  |SB |
  ------

class D(A):
    ------
    | SB|
    ------
"""
# WAP to create a chatbot system which follow its property instagram, over whatsapp, and snapchat, which work folow work on herarical 
#  inheitence 

'''class chat:
    contact={'sumit':[],'vivek':[],'satyam':[]}
    def to_send(self):
        name=input('Enter the name:- ')
        if name in self.contact:
            msg=input('enter the msg:-  ')
            self.contact[name]+=[msg]

        else:
            print('N/A')

class whatsapp(chat):
    pass

class snapchat(chat):
    pass

ob1=whatsapp()
ob1.to_send()
print(ob1.contact)'''


#----------------------
# Hybrid Inheritance
#----------------------
'''
-> it is a type of inheritance where we have more than one model in a single model 
-> these model are more efficent than normal model 

'''

#WAP to show calculator using the hybrid inheritance where you have to choose differentclass operation
"""  
class add:
    def add(self):
        return self.a + self.b
    
class sub:
    def sub(self):
        return self.a-self.b
class mul:
    def mul(self):
        return self.a * self.b
    
class div:
    def div(self):
        return self.a//self.b

class  calculator(add,sub,mul,div):
    def __init__(self,a,b):
        self.a=a
        self.b=b
ob1 = calculator(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
print(ob1.add())
"""


# Solution by sir by sir 

class addition :
    @staticmethod
    def add(a,b):
        print('add',a+b)
class subtraction:
    @staticmethod
    def sub(a,b):
        print('sub',a-b)


class new(addition,subtraction):
    @staticmethod
    def mul(a,b):
        print('mul',a*b)


class calaculator(new):
    @staticmethod
    def div(a,b):
        print('div',a/b)

calaculator.add(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
calaculator.sub(50,30)

