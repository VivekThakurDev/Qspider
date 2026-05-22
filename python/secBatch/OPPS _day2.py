
#-----------------
# constructor
#-----------------

# In opps whensever you wat to deal with object , you have to use self as per python standards.
# 
# 
"""syntax:-
Def __init__(self,args....):

""""""
class bank:
    bname='HDFC'
    bloc='Delhi'
    bIFSC=45457

def __init_(self,name,phno,acno,email,sal):
     """

"""
Method of Opps
it is phenomenon which is uses to access  the attribute  of class and object
we have three methods
1) Object Method
2) class method
3) static method 

1)  object method :- these are the method which are used to access, modify only object member in the persence of self
"""
"""
class company:
    cname='Vikas Pvt.Ltd'
    cloc='DDU'
    CCeo='Vivek'
    def __init__(self,name,phno,acno,email,loc,sal):
        self.name=name
        self.phno=phno
        self.acno=acno
        self.email=email
        self.loc=loc
        self.sal=sal

    def dis_obj(self):
        print(self.name,self.phno,self.acno,self.email,self.loc,self.sal)

    def ch_loc(self,new):
        self.loc=new

amit=company('Vivek',7452854,7485145,'amit@gmail.com','USA',7428574)
rahul= company('rahul',528555,75421,'vikash@gmailc.com','USA',74526)

print(company.cname,company.cloc,company.CCeo)
amit.dis_obj()
amit.ch_loc('India')
amit.dis_obj()
        

"""
"""

class Qspider:
    cname='Qspide'
    cbranch='Noida'
    c_loc='sec-3,noida'

    def __init__(self,name,phno,email,loc,stream,p_year,rating):
        self.name=name
        self.phno=phno
        self.email= email
        self.loc= loc
        self.stream=stream
        self.p_year=p_year
        self.rating=rating

    def display(self):
        print(self.name,self.phno,self.email,self.loc,self.stream,self.p_year,self.rating)
  
    def c_rating(self,new):
        self.rating=new
    
    def stream(self,new):
        self.stream=new
vivek=Qspider('vivek',74525885,'adjkhka@gmail','Ranchi','Data Analysis',2027,1)

print(Qspider.cname,Qspider.cbranch,Qspider.c_loc)
vivek.display()
vivek.c_rating(2)
vivek.display()

"""
#---------------
# Class method
#---------------
"""
# it is a method which is use to access, modify class member useing cls,a decorator @classmethod

syntax:-
@classmethod
def m_name(cls,...)



"""
"""
class Qspider:
    cname='qsipder'
    cbranch='Noida'
    c_loc='sec-3,noida'

    def __init__(self,name,phno,email,loc,p_year,rating):
        self.name=name
        self.phno=phno
        self.email= email
        self.loc= loc
        #self.stream=stream
        self.p_year=p_year
        self.rating=rating

    def display(self):
        print(self.name,self.phno,self.email,self.c_loc,self.p_year,self.rating)
  
    def c_rating(self,new):
        self.rating=new
    
    @classmethod
    def class_display(cls):
        print(cls.cname,cls.cbranch,cls.c_loc)

    @classmethod
    def cname(cls,new):
        cls.cname=new

    def stream(self,new):
        self.stream=new
vivek=Qspider('vivek',74525885,'adjkhka@gmail','Ranchi','Data Analysis',2027,1)

Qspider.class_display()
vivek.display()
vivek.c_rating(2)
vivek.display()


"""


#-------------------
# Static Method
#-------------------
''''
these are the methid which not belongs to any class or object but act as a supported method 

then no need of mention it self and cls  but we have to use a decorator @staticmethod
'''
"""
class Qspider:
    cname='qsipder'
    cbranch='Noida'
    c_loc='sec-3,noida'

    def __init__(self,name,phno,email,loc,stream,p_year,rating):
        self.name=name
        self.phno=phno
        self.email= email
        self.loc= loc
        self.stream=stream
        self.p_year=p_year
        self.rating=rating

    def display(self):
        print(self.name,self.phno,self.email,self.c_loc,self.stream,self.p_year,self.rating)
  
    def c_rating(self,new):
        self.rating=new
    
    @classmethod
    def class_display(cls):
        print(cls.cname,cls.cbranch,cls.c_loc)

    @classmethod
    def cname(cls,new):
        cls.cname=new
    @staticmethod
    def msg():
        print('good morning')
    def stream(self,new):
        self.stream=new
vivek=Qspider('vivek',74525885,'adjkhka@gmail','Ranchi','Data Analysis',2027,1)

Qspider.msg()
Qspider.class_display()
vivek.display()
vivek.c_rating(2)
vivek.display()

"""
# WAP a program of bank system using static method 
"""class bank:
    bname='BOI'
    banch='Noida'
    bIFSC='BKID000004454'

    def __init__(self,name,phno,email,accno,bal):
        self.name=name
        self.phno=phno
        self.email=email
        self.accno=accno
        self.bal=bal

    @classmethod
    def display_cls(cls):
        print(cls.bname,cls.banch,cls.bIFSC)

    def display(self):
        print(self.name,self.phno,self.email,self.accno,self.bal)

    
        

    def deposit(self,amt):
        self.bal= self.add(self.bal,amt)

    def withdraw(self,amt):
        if amt> self.bal:
            print('Insufficent Balance')
        else:
            self.bal=self.sub(self.bal,amt)

    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
vivek=bank('Vivek',7539518541,'Vivek4321@gmail.com',745214525,8000,)

bank.display_cls()  
vivek.display()
vivek.deposit(500)
vivek.display()
vivek.withdraw(4000)
vivek.display()

"""

# WAP a program to create a library system using use method like issue book and return book 
"""
class lib:
    libName='Nattional Library'
    libBranch='Noida'
    
    @classmethod
    def display_cls(cls):
        print


    def __int__(self, bookname,bookno,edition):
        self.bookname=bookname
        self.bookno= bookno
        self.edition=edition

    def book_dis(self):
        print(self.bookname,self.bookno,self.edition)

    def issue(self,no,issuebook):
        if issuebook != self.bookname:
            print('book not avilabel')
        else:
            self.bookno=self.sub(self.bookno,no)

    def deposite(self,no):
        self.no=self.sub(self.bookno,no)

    @staticmethod
    def add(a,b):
        return a+b
    
    @ staticmethod
    def sub(a,b):
        return a-b
book1=lib('C++',5,2005)

book1.book_dis()"""


class lib:
    book_dic={'python':20,'sql':10,'JAVA':15,'django':15}

    def __init__(self,name,phno,email,sid,book=[]):
        self.name=name
        self.phno=phno
        self.email=email
        self.sid=sid
        self.book=book


    def dis_obj(self):
        print(self.name,self.phno,self.email,self.sid,self.book)

    def issue_book(self):
        bn=input('enter the book.:- ')
        if bn in self.book_dic and self.book[bn]>0:
            self.book_dic[bn]-=1
        else:
            print('Book not found')


    def return_book(self):
        bn=input('Enter the rbook')
        self.book.remove(bn)
        self.book_dic[bn]+=1


ob1=lib('Vivek',753951585,'kvivek@gmailcom','Sid','python')

ob1.dis_obj()
