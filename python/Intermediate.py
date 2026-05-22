# Intermediate terminationd in looping:----
# Making the loops  to stop the execution in between and restricting them to all the interation 

##  Types :
## 1)  Break:- It is a keyword used to terminate the loop on current iteration 

## 2) Continue:-
#                It is used to skip the current iteration of loop.

# 3) Pass:-  
#It is used to make invalid block as a valid block



##  WAP to check  wheather the given string is having only lowercase charecter or not
'''
str=input('Enter the string')

for i in str:
    if 'A'<= i<='Z':
            print('Its containing the other than lowercase charecters as well ')
            break
  
'''
  


# WAP to check weather the given collection is having nested collection or not 

'''l= eval(input('Enter the collection'))
for i in l:
      if type(i) in [list,set,tuple,set,dict]:
            print('it has nested collection')
            break
else:
      print('it does not have nested collection')'''


## WAP to extract all the interger from the list
"""
lst= [1,2,True,4,'hello',5]
out=[]
for i in lst:
    if type(i) == int:
        out.append(i)
        continue
    
print(out)
        """

###  TO check the given input is prime or not
"""n= int(input('enter the interger number :- '))
for i in range(2, n):
    if n % i == 0:
        print(' not prime number')
        break
else:
    print('prime number')"""

### skip invalid user input
# if  input is not digit skip else store it into a lsit (take 5 input)

"""
out=[]
for i in range(5):
     In = input('enter the input :- ')
     if In.isdigit():
          out.append(In)
          continue
print(out)
"""

#   or 
"""
out=[]
i = 0
while i < 5:
    In = input('enter the input :- ')
    if In.isdigit():
        out.append(In)
        continue
    i+=1
print(out)

"""
#  skip the duplicate elements
"""
data = [1,2,2,3,4,4,5]
out=[]
for i in data:
    if i not in data :
        out.append(i)
        continue
print(out)

"""



# Write diffrence between while loop and for loop
"""While loop:
1) intiallization and updation is medantory in while loop
2) we cannot use while loop on set and dictionary
3) 


For Loop:
1) intiallization and updation is automated in for loop
2) it allow all the collection data type to use in for loop"""




