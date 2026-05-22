# # Spy number 
##prime number
# n= int(input('enter the number :- '))
# def armstron(n):
#     i=n
#     power=len(str(n))
#     total=0
#     while i!=0:
#         digit=i%10
#         total+=digit**power
#         i//=10
#     return total
# total = armstron(n)
# def check(total):
#     if total==n:
#         print('Armstrong')
#     else:
#         print('not Armstrong')
# check(total)


i=int(input('Enter the number:- '))
n = i
power= len(str(i))
total = 0
while n>0:
   
    digit = n%10
    total += digit **power
    n//=10
if i==total:
    print('Armstrong number')
else:
    print('Not Armstrong')