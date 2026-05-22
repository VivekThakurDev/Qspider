### wap to check weather the given data Uppercase,lower case,digit or digit or Special character:
'''
n = input('ente the char ')
if 'a' <= n <='z':
    print('it is lowercase')
elif 'A' <= n <='Z':
    print('it is Uppercase')
elif '0' <= n <= '9':
    print('it is number')
else:
    print('it is special char')
        
'''

### greatest among 4 number
'''
n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
n3 = int(input('Enter number 3: '))
n4 = int(input('Enter number 4: '))

if n1> n2:
    print ('nuber 1 is greater than n2')
elif n2> n3:
    print ('nuber 2 is greater than number 3')
elif n3> n4:
    print ('nuber  is greater than number 3')
else:
    print('greater than all')
'''

###  WAP to check weather the given integer is single digit or two digit or three
##    digits or more than three digits.
'''
n= int(input('enter the num :- '))
if 0<=n<=9:
    print('it is single digit number ')
elif 10<= n <= 99:
    print('double digit')
elif 100<= n <= 999:
    print('number is 3 digit')
else :
    print('Number is more than 3 digit ')
'''

# WAP to check the given point are lying in the which quadrant.
'''
X= int(input('enter the num1 :- '))
Y= int(input('enter the num :- '))
if X>0 and Y>0:
    print('1st quad')
elif X<0 and Y>0:
    print('2nd Quadrant')
elif X<0 and Y<0:
    print('3rd Quadrant')
elif X>0 and Y<0 :
    print('4th Quadrant ')
else:
    print('it might be posible ')
'''


###  WAP to find the samllest of 3


### Consider  a charecter input if it is upper case canvert it into  lowwercase,
#if it is lower case convert it into uppwecase , if it digit print the remainder when
## it is divided by 3 else if it is special charecter print it's ASCII value.
'''
n= input('enter the value')
if 'A' <= n <= 'Z':
    print('lower case of the char is :- ' , chr(ord(n)+32))
elif 'a'<=n<'z':
    print('upper case of the value is :- ', chr(ord(n)-32))
elif '0'<=n<='9' :
    if int(n)%3 != 0 :
        print(' Remainder when remainder whenit is divided by 3:- ', int(n)%3)
else:
    print("it is special charecter print it's ASCII value:- ", ord(n))

'''


###WAP to print 'Fizz' if the given number is  given number is multiple of 3 digit print
# 'Buzz' if the givennumber is multiple of 5 and print 'Fizbuzz' i


n= int (input('enter the number '))
if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0 :
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print('number is not divided by bot 3 and 5')
















