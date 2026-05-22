# prime of prime
# Sum of digits of a prime number must be prime number
#                  Example :-prime of prime between 1 to 30  (2,3,5,7,11,23,29

# def primeofprime(n):
#     if n==2 or n==3 or n==5 or n==7:
#         return 'prime number'
#     for i in range(2,n):   
#         if n%i==0:
#             return 'Not Prime '
#         return 'prime' 
    
# print(primeofprime(13))


# def checkprimeofprime(n):
#     num=n
#     count=0
#     while n!=0:
#         ld=num%10
#         count+=ld
#         num=num//10
#     if count ==  num:
#         return 'Prime Of Prime'
#     return 'Not Prime Of Prime'

# print(checkprimeofprime(13))

#---------------
# solution
#--------------
"""
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        return True
 """   
def sum_digit(num):
    sum = 0
    while num != 0:
        ld = num % 10
        sum += ld
        num = num//10
    return sum
"""
def prime_of_prime(n):
    for i in range(1,n+1):
        if is_prime(i) and is_prime(sum_digit(i)):
            print(i)
        
print(prime_of_prime(30))

"""

# ----------------
# Sum of digits till single digit 
#------------------
"""
def sum_till(num):
    while num>9:
        num= sum_digit(num)
        return num
    
print(sum_till(719))
"""

# Count the frequency of word in a given string 
# output ={'we':2,'are':2 ,'what':1}
def countfreq(string):
    s=string.split()
    out={}

    for i in s:
        if s[0] not in out:
            

s= 'We are what we are'