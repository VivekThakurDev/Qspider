# def pattern(n):
#     if (n%2==0):
#         print('Pattern  is not possible')
#         return;
#     mid= n//2+1
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i==mid or j == mid:
#                 print('* ', end='')
#             else:
#                 print('  ', end='')
#         print()

# n = int(input('enter the number of rows:- '))
# pattern(n)
"""   
    *     
    *     
* * * * * 
    *     
    * """




# def pattern11(n):
#     mid = n//2+1
#     for i in range (1,n+1):
#         for j in range(1,n+1):
#             if i==mid or j == mid & i==1 or j<mid :
#                 print('* ', end='')
#             else:
#                 print('  ',end='')
#         print()   

# n =int (input('Enter the number:- '))
# pattern11(n)



#For different pattern 

"""

*
* *
* * *
* * * * 
* * * * *
"""
#GO THOUGH
"""
patternsize 
for loop 
for loop
     print(* )"""
"""
      * 
   *  *  *
"""
# space = n-1 , pattern size
# loop=1 for i in range (1,n)
#  loop=2 for j in range(1, space) // 
#             print(' ')       // this is for space 
#  loop=3 for j in range(1,n+1)  // loop 2, 3 both will build on same line/same iteration 
#  print('*')              // this loop for print pattern 
#  space -=1  , patternsize +=2               // in every iteration we have to decrese

       
def hammingWeight(n):

    count=0
    while n !=0:
        if (n & 1) == 1:
            count +=1
        n >>=1
        return count
    
n = int(input('Enter the number:- '))
print(hammingWeight(n))