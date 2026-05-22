############ if condtion

#   Program to check  wheather the number is even
'''
n= int(input('enter the number '))
if n%2 ==0:
    print('even')
'''

############
##  program to check  wheather the string has exactily 5 char in it
'''
n= input("enter the char :- ")
if len(n) == 5:
    print('string has exactly 5 char')
'''

##### program to check wheather the number is greater than 200
'''
n = int(input('enter the number '))
if  n > 200:
    print('number pura 200 se jada hai ')
else :
     print('Dekho yesa hai lun lelo ')

'''


## program to print  the square of number only if it is multiple of 3
'''
n= int(input('enter the number '))
if n%3 ==0:
    print('square  of the number is :', n**2)
else:
    print('number adhura hai ')
'''

###  program to check the number is two degit number or not
'''
n= int(input('enter the number '))

if n>9 and n<100:
    print('number is two digit number')
else:
    print('number is not two digit number')

'''
### program to check  whether the char is vowel  or not
'''
a= ['a','i','e','o','u']
n= input('enter the char ')
n.upper()
if n in a:
    print('vowel hai bhai ')
else:
    print('vowel nai hai bhai')
'''

### Program to print ascii value of a character only if it is upper case

n= input('enter the char ')
if n<= 'A' <= 'Z':
    print(ord(n))


### WAP to print the chube of the number only if it is divivsible by 9 or 6.
'''
n= int(input('enter the number '))
if n%9==0 or n%6==0:
    print('ladle satisfied kar gaya ,'n**3)
else:
    print('bhdk number change kar ')
'''

###  WAP to chaek wheather the given number is Digit Number 
'''
n= int(input('enter the number ')) 
if 100<= n<=999:
    print( 'kya bidu satisfied kar gaya')
'''


#####
### WAP to check the last digit of a giving number is 5
'''
n = int(input('enter the number '))
if n%5==0 or n%5 == 5:
    print('number haiu ')
    '''


### Wap to check weathe the given data id float


# or
'''
n= eval(input('Enter the data '))
if n in float:
 print('data si float')
print(type(n))
'''


#### WAP to check weather the data is single value data .
'''
n= eval(input('Enter the data '))
if type(n) in [float,complex,bool,int]:
    print('it belong to digit ')
'''

#### WAP to check weather the given number is digit or not.
'''
n = input('entet he number')
if '0' <= n <='9':
    print('the given char is  digit ')
    
'''
