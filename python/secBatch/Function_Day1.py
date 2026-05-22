#---------------
#Function 
#---------------
'''
-> function is a block of code which  contain set of instruction and work while calling
-> we use function to avoid repetation code and reduce the code size.
-> we have two type of function 

1) inbuild function 
2) user-define 
'''
# inbuild function  :- these are the pre deine function which have specific task to do so you dont't have to write script for inbuit function

# user-define :- the function which is created as per user requirement that function are known as user function
"""
create user define function we use keyword that is def 

"""
# there are four type of user define 
"""1) without argument without return value 
2) with argumnent without return value 
3) without argument with return value
4) with argument with return value"""

#---------------------------------------
# without argument without return value 
#----------------------------------------

# WAP to extract all the uppercase alphabate from the string 

"""def up():
    str=input('Enter the string :- ')
    out=''
    for i in str:
        if 'A'<=i<='Z':
            out+=i
    print(out)

up()
"""
#WAP a program to sum of number present in the Email_ID

def email():
    a=input('Enter the email-id:- ')
    b=0
    for i in a:
        if "0"<= i<= "9":
            b+=int(i)
        
    print(b)

email()



