#-----------------------
# Fundamentals of OPPS
#-----------------------
"""
As we know OPPS is the relationship between class and object where it follows some fundamentals which is workable 
on real time sceaniores

We have four type of fundamentals
1) Encaplsulation
2) Inheritance
3) Polymorphism
4) Abstraction

"""

#-------------------
#Encaplsulation
#-------------------
'''
It is a properties of OOPS where we bind the data at methods into single unit which is called class. 
-> to resictist direct assecc some of the components which pervent accedental modification in the single unit 
-> In python to implement encapsultion we use access specifier 
->   we three type of access spicifier 
  1) public
  2) private(semi public )
  3) protector 
    ------------------
    |   methods|  data|
    -------------------



'''

#------------
#public
#--------------
'''
it is the access specifier where we can access the data inside the class and outside the class
'''
# Example of public access specifier 
""""
class collage:
    cname='CU'
    loc='Punjab'

    def __init__(self,name,phno,SID,stream,passout_year):
        self.name=name
        self.phno=phno
        self.SID=SID
        self.stream=stream
        self.passout_year=passout_year

    def display(self):
        print(self.name,self.phno,self.SID,self.stream,self.passout_year)
    
    @classmethod
    def cls_display(cls):
        print(cls.cname,cls.loc)

vivek=collage('vivek',475235,23100010132,"CSE",2027)

vivek.display()
vivek.cls_display()
"""
#------------
# Protected
#------------
"""
it is a access specifier where we give security in the form of semisecurity using single underscore
before the members """
"""

class collage:
    cname='CU'
    loc='Punjab'

    def __init__(self,name,phno,SID,stream,passout_year):
        self.name=name
        self.phno=phno
        self.SID=SID
        self.stream=stream
        self.passout_year=passout_year

    def display(self):
        print(self.name,self.phno,self.SID,self.stream,self.passout_year)
    
    @classmethod
    def cls_display(cls):
        print(cls.cname,cls.loc)

vivek=collage('vivek',475235,23100010132,"CSE",2027)

vivek.display()
vivek.cls_display()
print(collage.cname)"""

#-------------------
# Private specifier
#-------------------

''''
it is a acess spicifer where we give a complete a security or complete protection to a single identity to 
using private acess specifier 

-> We use double underscore while giving security 
'''
class collage:
    cname='CU'
    __loc='Punjab'

    def __init__(self,name,phno,SID,stream,passout_year):
        self.name=name
        self.phno=phno
        self.__SID=SID
        self.stream=stream
        self.passout_year=passout_year

    def display(self):
        print(self.name,self.phno,self.__SID,self.stream,self.passout_year)
    
    @classmethod
    def cls_display(cls):
        print(cls.cname,cls.__loc)

vivek=collage('vivek',475235,23100010132,"CSE",2027)

vivek.display()
vivek.cls_display()
print(collage._collage__loc)# class method
print(vivek._collage__SID) #objectMethod