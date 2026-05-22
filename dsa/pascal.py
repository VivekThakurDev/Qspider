# def pascal(n):
#     comb=1
#     print(comb,end='   ')
#     for i in range(0,n):
#         comb= comb*(n-i)//(i+1)
#         print( comb,end='   ')



# def pascalPattern(n):
#     for i in range(0,n+1):
#         space=n
#         for j in range(0,space):
#             print(end='    ')
#         pascal(i)
#         space=n-i
#         print()
# pascalPattern(5)

# &&&&&&&&&&&&&&&&&&&&&  correct pyramid
"""def pascal(n):
    comb = 1
    print(comb, end='  ')
    for i in range(0, n):
        comb = comb * (n - i) // (i + 1)
        print(comb, end='  ')
def pascalPattern(n):
    for i in range(0, n + 1):
        for j in range(0, n - i):
            print("  ", end='') #print space
        pascal(i)
        print()
n= int(input("Enter the number of rows: "))
pascalPattern(n)

"""
#WAP to print each digit of  left to right by using recursion 

"""def leftToRight(n):
    if n ==0:
        return
    leftToRight(n//10)
    print(n%10)
leftToRight(245)
"""
"""
# Output:- 
2
4
5
"""
# greatest number of  two variable
"""
def big(a,b):
    return a if a>b else b
print(big(10,60))
"""
# greatest number more than two variable
"""
def big(a,b):
    return a if a>b else b
a=10
b=30
c=5
d=50
e=2
f=55
biggest= big(big(a,b),big(c,big(d,big(e,f))))
print(biggest)

"""

#### sum of cubes if number from 1 to 100 by using recursion
"""
def sum(n):
    if n==1:
        return 1
    return n+ sum(n-1)   
n = int(input('Enter the last number:- '))
print(sum(n))
"""
#### sum of cubes if number from 1 to 100 by using recursion
"""
def sumofcube(n):
    if n==1:
        return 1
    return n**3+ sumofcube(n-1)   
n = int(input('Enter the last number:- '))
print(sumofcube (n))
"""
#### sum of factorial if number from 1 to n by using recursion
"""
def sumoffact(n):
    if n==1:
        return 1
    return n*sumoffact(n-1)   
n = int(input('Enter the last number:- '))
print(sumoffact (n))
"""


##### calculate power

"""
def getpower(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    return a*getpower(a,b-1)    
sum=getpower(3,2)
print(sum)
"""

# fibbonacci by recurision
"""
def fibbonacci(n):
   if n==0 or n==1:
      return n
   return fibbonacci(n-2)+fibbonacci(n-1)
print(fibbonacci(4))"""

## WAP to take a inputs and print HCF of the two numbers.
"""
def getHCf(a,b):
    if a==0:
        return b
    return getHCf(b%a,a )
x=36
y=35
hcf= getHCf(x,y)
print(hcf)

"""


## tower of hornoi
def toh(n,source,aux,destination):
    if n==1:
        print(f"Move disk from {source} to {destination}")
        return
    toh(n-1,source,destination,aux)
    print(f'Move disk from {source} to {destination}')
    toh(n-1,aux,source,destination)
n=int(input('Enter number of disk:- '))
toh(n,'A','B','C')