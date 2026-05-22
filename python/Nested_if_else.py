## WAP to create a login Page
'''
User_name = 'Vivek'
password='vuvek@123'

Un = input('enter the user name : ')


if Un == User_name :
    ps = input('entert the pass word: ')
    if ps== password:
        print('Welcome')
    else:
        print('Wrong PassWord')
else: 
    print('Invalid User')
    '''

## WAP to print the middle value of a list only if it is string 
'''
l = eval(input('enter the list : '))
if len(l)% 2 != 0:
    if type(l[len(1)//2])==str:
        print(l[len(l)//2])
    else:
        print('the middle value is not string')
else:
    print('the list has even number of elements')

'''

### WAP to check weather the character us vowel or consonent.
'''
ch = input('enter the character : ')
if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    if ch in 'aeiouAEIOU':
        print('vowel')
    else:
        print('consonent')
else:
    print('invalid character')

'''

## WAP to find the greatest of 4  numbers. (without using and operator only using nested if else)
'''
a = int(input('enter the first number : '))
b = int(input('enter the second number : '))
c = int(input('enter the third number : '))
d = int(input('enter the fourth number : '))
if a > b:
    if a > c:
        if a > d:
            print(a, ' a is greatest')
        else:
            print(d ,' d is greatest')
    else:
        if c > d:
            print( c ,' c is greatest')
        else:
            print( d  , ' d is greatest')
elif a < b:
    if b > c:
        if b > d:
            print('b is greatest')
        else:
            print('d is greatest')
    else:
        if c > d:
            print('c is greatest')
        else:
            print('d is greatest')
else:
    print('all numbers are equal')
'''

###WAP to print the last value of a list only if it is plandrome string starting with vowel.
'''
lst=[True,2.4,33,3-9j,'eye']
vowel='aeiouAEIOU'
if type(lst[-1])==str:
    if lst[-1][0] in vowel:
        if lst[-1] == lst[-1][::-1]:
            print(lst[-1])
        else:
            print('the last value is not a plandrome string')
    else:
        print('the last value is not starting with vowel')
else:
    print('the last value is not a string')
    '''
##### WAP to print the reverse  string only if it is starting with vowel , ending with constant and having a middel value

'''''

str= input('enter the string : ')
vowel = 'aeiouAEIOU'
if str[0] in vowel:
    if str[-1] not in vowel:
        if len(str) % 2 !=0:
            print(str[::-1])
        else:
            print('the string does not have a middle value')
    else:   
        print('the string does not end with a consonent')
else:
    print('the string does not start with a vowel')
    '''


### WAP to find the second greatest of 4 values (can use and operator and nested if else , elif ladder)
'''
a = int(input('enter the first number : '))
b = int(input('enter the second number : '))    
c = int(input('enter the third number : '))
d = int(input('enter the fourth number : '))

if a > b and a > c and a > d:
    if b > c and b > d:
        print('second greatest is : ',b)
    elif c > b and c > d:
        print('second greatest is : ',c)
    else:
        print('second greatest is : ',d)
elif b > a and b > c and b > d:
    if a > c and a > d:
        print('second greatest is : ',a)
    elif c > a and c > d:
        print('second greatest is : ',c)
    else:
        print('second greatest is : ',d)    
        '''