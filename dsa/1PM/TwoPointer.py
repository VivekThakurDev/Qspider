
# Move Zero  leetcode 
"""
def movzero(num):
    i=0
    j=0
    
    while j< len(num):
        if num[j] !=0 :
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
            i+=1
        j+=1
    return num
n = [1,0,1,0,0,0,2]
print(movzero(n))   

# Output:- [1, 1, 2, 0, 0, 0, 0]4

"""


# 
"""
def movzero(num):
    i=0
    j=0
    
    while j< len(num):
        if num[j] ==0 :
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
            i+=1
        j+=1
    return num
n = [1,0,1,0,1,0]
print(movzero(n))   

#output :- [0, 0, 0, 1, 1, 1]"""


#---------------
#  Dutch national flag  aglorithm
#---------------
# logic:
'''
low=0
mid=0
high=lenght(number)-1
loop (while (mid<=high))
if midvalue==0
swap(low,mid)
low++
mid++
else if   midvalue==1
mid++
esle
swap(mid,high)
high--
'''

#-------------
# solution 
#------------
"""
def sortcolor(num):
    low=0
    mid=0
    high=len(num)-1
    while mid<=high:
        if num[mid]==0:
            swap(num,low,mid)
            low+=1
            mid+=1
        elif num[mid]==1:
            mid+=1
        else:
            swap(num,mid,high)
            high-=1
    return num

def swap(num,i,j):
    temp=num[i]
    num[i]=num[j]
    num[j]=temp


n=[2,0,2,1,1,0]
print(sortcolor(n))

"""


#------------------
# Two Sum
# ----------------
#algo
# 
def twosum(num,target):
    low=0
    high= len(num)-1
    while low<high:
        total= num[low]+num[high]
        if total==target:
            return (low-1, high+1)
        elif total<target:
            low+=1
        else:
            high -=1

    return 
    
n=[20,3,2,12,23,15] 
target= 25
print(twosum(n,target))          

