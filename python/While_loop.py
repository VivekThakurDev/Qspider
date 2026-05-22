### Write ap program to reverse the given number (without typecasting)
'''
num = int(input('entert the number :- '))
rev=0
while num>0:
    rem = num%10   # remender 
    rev= rev*10+rem  # reverse 
    num= num//10       # updation 
print('Reverse num: ',rev)

'''

### WAP to to sum of individual digit of a number 
'''
num= int (input('enter the number :- '))
sum=0
while num>0:
    rem = num%10
    sum = sum +  rem
    num= num//10
print('sum of number : ', sum)

'''

### WAP to extract all even integers  present in a tuple at odd index
'''
t = eval(input('enter the tuple:- '))
out=[]
i=0
while i<len(t):
    if type (t[i]) == int:
        if i%2 != 0 and t[i] % 2 == 0:
            out.append(t[i])
    i+=1
print(out)

'''
### WAP to remove duplicates from a list without converting into set
'''
l= eval(input('Enter the list :- '))
out=[]
i=0
while i<len(l):
    if l[i] not in out:
        out.append(l[i])
    i+=1
print(out)
    
'''







###  WAP to find the sum of all the  odd number between the given range 
"""
s= int (input('Enter the number'))
e= int (input('Enter the ending number '))

total= 0
i=s
while i<=0:
    if i%2 != 0:
        total +=i
    i+=1
print(total)

"""
### WAP to find the greatest number un a given list of integers.
'''

l=[2,45,2,2,4,5,676,6,33,22,9,488,90,24]

greatest = l[0]
i=0
while i<len(l):
    if l[i]> greatest:
        greatest  = l[i]
    i+=1
print(greatest)
'''

### WAP to find the sum of cube of a number in a string .
'''
em= 'Vivek71@gmail'
i=0
sum=0
while i<len(em):
    if '0' <=em[i]<='9':
        sum +=int(em[i])**3
        
    i+=1
print(sum)

'''







### WAP to  find the HCF of two numbers
# a = int(input('enter the number:- '))
# b = int(input('Enter a second number :- '))
# HCF= i=1
# small=0
# if a > b:
#     small= a
# else:
#     small=b
# while i< small:
#     if a%i==0 and b%i==0:
#         HCF =i
#     i+=1
# print(HCF)


### WAP to check weather the number is palindroms or not 
'''
n= int(input('Enter a number :- '))
rev= 0
temp=n
while temp>0:
    rem = temp%10
    rev= rev*10 + rem
    temp = temp//10
if rev == n :
    print('Palindrom')
else:
    print('Not plaindrom')
'''


### WAP to check the given number is prime or not 
'''

n = int(input('Enter the number'))
o=0
i=2
while i< n:
    if n % i ==0:
        o=1

    i+=1
if o==1:
    print(" Not prime")
else:
    print("Prime")

'''

###WAP to check weather the number is Armstrong  or not 

'''
i=int(input('Enter the number:- '))
n = i
power= len(str(i))
total = 0
while n>0:
   
    digit = n%10
    total += digit **power
    n//=10
if total  == i:
    print('Anrmstrong Number')
else:
    print('not Armstrong')

'''

## WAP to check the number is strong or not 
"""
n= int(input('enter the number :- '))
num=n
to =0
while n !=0:
    Id = n % 10
    fact =1
    for i in range(1,Id+1):
        fact*=i
    to+=fact
    n = n // 10

print(sum)
if num == to:
    print(' Strong')
else:
    print('not Strong')

"""


#### check wether the number is perfect number or not 
'''
n = int(input('enter the number :- '))
total=0
i=1
while i<n:
   if n%i== 0:
      total +=i
   i+=1
if total ==n:
   print('Perfect')
else:
   print('Not')
'''

## WAP to find the product of all the digits present in a number.

### WAP to count the nmber of the string 


n = 27
total = 0
i=1
while i<n:
   if n%i==0:
        total+=i
        i+=1
if  n ==total:
    print('prime')
else:
    print('not prime')