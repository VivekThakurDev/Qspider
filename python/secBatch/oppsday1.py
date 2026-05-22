"""class zoo:
    a='ape'
    b='bat'
    c='cat'

sub=zoo()
obj2=zoo()

# print(zoo.a,zoo.b,zoo.c)
# print(sub.a,sub.b,sub.c)
# print(obj2.a,obj2.b,obj2.c)


zoo.a= 'jadu'
print(zoo.a,zoo.b,zoo.c)
"""
#-------------------
# member of object
#-------------------

"""
these are the properties which belongs to class and object

-> there are two type of members
1)  static member :- these property belongs to class( Example :- school name, collage name )
2) object member  :- these property belong to object ( Example :- )


"""

#Q. write a program to create a class bank minimum 3 class memeber 2 object  with minimum 4 object member
"""
class bank :
    bname='BOI'  # static  member
    bloc='Noida'
    bIFSC='BKID0000000044'


vivek=bank()
sujal=bank()

vivek.name='Vivek'
vivek.Acc_No=7539521287426874   # object memeber
vivek.loc='Ranchi'
vivek.phno=7585749685

print(bank.bname,bank.bloc,bank.bIFSC)
print(vivek.name,vivek.Acc_No,vivek.loc,vivek.phno)
print(vivek.bname,vivek.bIFSC)
"""
#Q WAP to create a class hospital with minimum 3 class memmber with 2 object  with minimum 7 object member 
"""
class hospital:
    Hname='apolo'
    Hbranch='Noida'
    HState='UP'

dental=hospital()
emer=hospital()

dental.patientName='Vivek'
dental.age='22'
dental.Pno=7539854174
dental.fname='wdwsdfes'
dental.PAdress='Ranchi'
dental.Doa='23-2-2026'
dental.prob='dental'
dental.nextDate='20-5-2026'

print(dental.Hname,dental.Hbranch,dental.HState)"""



#--------------
# Opps with function
#---------------

class bank :
    bname='BOI'  # static  member
    bloc='Noida'
    bIFSC='BKID0000000044'

    def detail(self,name,phno,loc,accno,email):
        self.name=name
        self.phno=phno
        self.loc=loc
        self.accno=accno
        self.email=email

    def display(self):
        print(self.name,self.phno,self.loc,self.accno,self.email)

vivek=bank('vivek')
sujal=bank()

bank.display()
# vivek.detail('vivek',7598518,'No',7452585,"shalhdla@gmail.com")
# sujal.detail('sujal',7529651,'Noida',7452585,'sujal@gmail.com')
# print(sujal.name,sujal.phno,sujal.loc,sujal.accno,sujal.email)
# print(vivek.name,vivek.phno,vivek.loc,vivek.accno,vivek.email)
# print(bank.bname,bank.bloc,bank.bIFSC)
# print(vivek.bname,vivek.bIFSC)


