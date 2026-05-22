"""# 
Bitwise NOT:-              
         it is used to flip all binary bits of a number from zero to one and one to zero.

"""
# Example:- 
# a=8
# b=-175
#print(~a)   """ output:- -9"""
#print(~b)    """ output:- 174"""




# Bitwise left  Shift(>>):-
""" 
Bitwise left  Shift(>>):-
                   it is used to shift the  binary bits of a number  k position  to left side 


            formula:-  (n<<k  => n*2^k)   
# Example:-
a=8
b=2
print(a<<b)    output:- 32               
"""

# Bitwise right Shift(>>):-
'''
Bitwise right Shift(>>):-
                   it is used to shift the  all binary bits of a number  k position  to right side

            formula:-  (n>>k  => n/2^k)

# Example:-
a=8 
b=2
print(a>>b)    output:- 2
'''
"""
#  leetcode 191:
n= 43
count=0
while (n!=0):
    if (n&1)==1:
         count+=1
    n=n>>1
print(count)
"""

# Bitwise  unsigned Right shift(>>>) or zero fill right shift:-

'''
this operator to used to shift the binary bit of operation to right while filling from zero MSB
it is use in java and c++ but not in python
'''

#leetcode 136
# leetcode 231 
# leetcode 50
#  if n<=0;                  
# return False

# 