# Inheritance 
'''
it is a phenomena where one class deviate properity to another class 
-> the class which deviate its property is called deviatent /parent class / super class
-> the class which acquired the properity is known as child class / derived class/ sub class


# we have five type of inheritance
1) single level inheritance 
2) multilevel inheritance
3) multiple inheritance 
4) heriarical Inheitance 
5) Hybrid Inheritance
'''

#-------------------------
# single level inheritance 
#--------------------------
"""
-> It is a phenomina where parent class deviate its properity to the child class
-> 
"""
# Constructor chainnig :- it is a phenomena where constructor of one class deviated to another class
#                          using super() method 
#                     syntax:- super().__init__(arguments)

# method chainning: it is a phenomena  where we deviate method of one class to another class using super() method
#                   syntax:- super().m_name(arguments)
#Example 
"""
class A:
    a=10
    b=20
class B(A):
    c=30
    d=40

print(A.a,B.b)
print(B.c,B.d,B.a)"""

# WAP to show single level inheritance in bank 
"""
class online:
    bname='SBI'
    bloc='Noida-3'
    bIFSC='SBIN00004545'

    def __init__(self,name,phno,email,addr,accno):
        self.name=name
        self.phno=phno
        self.email=email
        self.addr=addr
        self.accno=accno

    def disp_obj(self):
        print(self.name,self.phno,self.email,self.addr,self.accno ,end=' ')

class offline(online):
    def __init__(self,name,phno,email,addr,accno,addhar,PAN):
        super(). __init__ (name,phno,email,addr,accno)
        self.addhar=addhar
        self.PAN=PAN

    def disp_obj(self):
        super().disp_obj()
        print(self.addhar,self.PAN)

offline1=offline('vivek',475235,'vivek@gmail','Ranchi',23100010132,123456789012,'ABCDE1234F')

offline1.disp_obj()


"""
#--------------------------
#Multilevel Inheritance 

"""
It is a type of inheritance where parent deviate it properties to child class is called multilevel 
inheritance

the lower class will aquire the properties of all the above classes 
it is a downward directional model 
"""
# WAP to show multilevel inheitance in education system

"""class tenth:
    
    def __init__(self,name,phono,add,tenthmark):
        self.name=name
        self.phono=phono
        self.add=add
        self.tenthmark=tenthmark



    def dis_obj(self):
        print(self.name,self.phono,self.add)
#t= tenth('vievek',7421552,'aefsfsfd')

class inter(tenth):

    def __init__(self,name,phono,add,tenthmark,collagename,twe_mark):
        super().__init__(name,phono,add,tenthmark)
        self.collagename=collagename
        self.twe_mark=twe_mark

    def dis_obj(self):
        super().dis_obj()
        print(self.collagename,self.twe_mark)

class grad(inter):
    def __init__(self,name,phono,add,tenthmark,collagename,twe_mark,university,CGPA):
        super().__init__(name,phono,add,tenthmark,collagename,twe_mark)
        self.university=university
        self.CGPA=CGPA

    def dis_obj(self):
        super().dis_obj()
        print(self.university,self.CGPA)

vivek=grad('vivek',74525885,'Ranchi',85,'CU',90,'CU',9.5)

vivek.dis_obj()

 """


# WAP to show multilevel inheritance in train reservation system
class train:
    def __init__(self,T_Name,T_No):
        self.T_Name=T_Name
        self.T_No=T_No

    def disp_tr(self):
        print(self.T_Name,self.T_No,end=' ')

class passenger(train):
    def __init__(self, T_Name, T_No,P_Name,P_Add,P_Phono,P_Seat):
        super().__init__(T_Name,T_No)
        self.P_Name=P_Name
        self.P_Add=P_Add
        self.P_Phono=P_Phono
        self.P_Seat=P_Seat

    def disp_pass(self):
        super().disp_tr()
        print(self.P_Name,self.P_Add,self.P_Phono,self.P_Seat,end=' ')

class ticket(passenger):
    def __init__(self, T_Name, T_No, P_Name, P_Add, P_Phono, P_Seat,T_PNR,T_Class,T_Price):
        super().__init__(T_Name, T_No, P_Name, P_Add, P_Phono, P_Seat)
        self.T_PNR=T_PNR
        self.T_Class=T_Class
        self.T_Price=T_Price

    def disp_ticket(self):
        super().disp_pass()
        print(self.T_PNR,self.T_Class,self.T_Price,end=' ')

P1=ticket('Jummu Tawi',12058,'Vivek','Ranchi','1234567890',25,1200045,'1st AC',4500)
P1.disp_ticket()