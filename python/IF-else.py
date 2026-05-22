
### WAP to check weather the given data ois float dat or not
'''
n = eval(input('enter the number :- '))
if type(n) == float:
    print('data is float')
else :
      print('the data is not of flaot')
'''


### WAP to check the string is plandrom or not 
'''
n = input('enter the string:- ')
if n == n[::-1]:
    print('number is plandrom')
else:
    print('is not plandrom')
    
'''


#### WAP to check Weather the data us mutable or not 
'''
n = eval(input('enter the string:- '))
if  type(n) in [list,set,dict]:
    print('it is mutable')
else:
    print('is not mutable')


'''
### WAP to check weather the charecter is digit or not 

'''
n = input('enter the string:- ')
if '0'<= n <= '9':
    print(' char is Digit')
else:
    print('is not Digit ')
'''


#### WAP to check waether the given charecter is special charecter or not.
'''
n = input('enter the Charecter :- ')
if n in ['~','#','$','%','^','&','*','_','-','+']:
         print('char is special')
else:
    print('char is not special')
'''

# OR
'''
n = input('enter the Charecter :- ')
if 'a'<=n <='z' or 'A' <=n <='Z' or  '0' <= '9':
    print('char is  not special')
else:
    print('char is special')
'''

### WAP to check weather a list consist of middle value or not
'''
n = eval(input('enter the collecting'))
if len(n)%2 != 0:
    print('it not consist a middel value')
else:
    print('it consist middel value')
'''
###
'''
n = int(input('enter the number '))
if n%2 == 0:
    print('number is even')
else:
    print('not even')'''

### WAP to check the  2 value  are pointing to same memory oe not
'''
n1= int(input('enter the value 1 '))
n2= int(input('enter the value 1 '))
if id(n1) == id(n2):
    print('same')
else:
    print('not same')
    '''
    
#### A consider a tuple of length 2 and check weather the tuple is homogenouse or not
'''
l =('hshkjf',2)
if type(l[0])==type(l[1]):
    print('homo')
else:
    print('not homo')

'''
### WAP to check waethe number is  positive or negative
'''
num =int(input('enter the number '))
if num >= 0:
    print('positive')
else:
    print('-ve')
'''
