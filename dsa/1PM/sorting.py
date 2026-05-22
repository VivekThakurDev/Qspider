# bubble sort
"""
def bubbleSort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                count+=1
    return a

l=[5,24,8,5,74,6,9]
print(bubbleSort(l))

time complexit=O(n^2)
space complexit=O(1)"""

# selction sort
"""
def selectionSort(a):
    n=len(a)
    for i in range (0,n):
        minIndex=i
        minValue=a[i]

        for j in range(i+1,n):
            if a[j]<minValue:
                minIndex = j
                minValue=a[j]
        
        a[minIndex]=a[i]
        a[i]=minValue

    return a
l=[6,45,7,5,4,1,5,8]
print(selectionSort(l))"""


# insertion Sort
"""
#pivot element = important element
def insersectionSort(a):
    for i in range(1,len(a)):
        pivot =a[i]
        j=i-1
        while j>=0 and a[j]>pivot:
            a[j+1]=a[j]
            j-=1
        a[j+1]=pivot
    return a
l=[6,45,7,5,4,1,5,8]
print(insersectionSort(l))

"""

#-------------
# Merge sort
#-------------
'''
-> it is a sorting algorithm works on divide and concore mecanism
-> first array is divided and then its element are merged in sorted manner
-> time to divide the array = log base 2 (n)
-> time to merge the array = n
-> O(time)=O(nlog2n)
-> O(space)= O(n)
'''
# merge two sorted array
"""
def mergeSort(a,b):
    merge=[0]*(len(a)+len(b))
    index1 = 0
    index2 = 0
    index3 = 0
    while(index1< len(a) and index2<len(b)):
        if a[index1]< b[index2]:
            merge[index3] = a[index1]
            index1 += 1
            index3 += 1

        else:
            merge[index3] = b[index2]
            index2 += 1
            index3 += 1
        
    while(index1 < len(a)):
        merge[index3]=a[index1]
        index3 += 1
        index1 += 1
    while (index2 <len(b)):
        merge[index3]=b[index2]
        index2 +=1
        index3 +=1

    return merge
a=[1,2,5,6,7,8]
b=[9,10,11,12]
print(mergeSort(a,b))  
"""
#[1, 2, 5, 6, 7, 8, 9, 10, 11, 12]
# time complexity = O(n+m)
# space complexity = O(n+m)    

# leetcode 88. Merge Sorted Array
"""
def merge(a,start,mid,end):
    merged=[0]*(end-start+1)
    indx1=start
    indx2=mid+1
    indx3=0
    while indx1<=mid and indx2<=end:
        if a[indx1]<=a[indx2]:
            merged[indx3]=a[indx1]
            indx3+=1
            indx1+=1
        else:
            merged[indx3]=a[indx2]
            indx3+=1
            indx2 +=1
    while(indx1<=mid):
        merged[indx3]=a[indx1]
        indx3+=1
        indx1+=1
    while(indx2<=end):
        merged[indx3]=a[indx2]
        indx3+=1
        indx2+=1
    for i in range(len(merged)):
        a[start+i]=merged[i]


def divide(a,start,end):
    if start<end:
        mid=(end+start)//2
        divide(a,start,mid)
        divide(a,mid+1,end)
        merge(a,start,mid,end)  


nums=[52,5,6,8,45,75]
divide(nums,0,len(nums)-1)
print(nums)
"""



#-----------
#Quick Sort
#-----------



#--------------
# bucket sort
#--------------

"""
G= [27,25,38,32,12,8,6,15,17]
G= [27,25,38,32,12,8,6,15,17]
step1:- 

idetify the min and max
min=
max=


Step:-2
decide the bucket requirement

bucketSize=
bucket required=(max-min)//bucketsize+1

step 3 :-
take no of bucket as per calculated in step 2

bucket0 [0-9] =[8,6]
bucket1 [10-19]=[12,15,17]
bucket2 [20-29] =[27,25]
bucket3 [30-39] = [38,32]
bucket3 []

step 4:-  
sort each  bucket
bucket0  =[6,8]
bucket1 =[12,15,17]
bucket2 =[25,27]
bucket3 = [32,38]

step 5:- 
merge  each bucket and copy it back to orginal array


"""

#----------------
# Tim Sort 
#---------------

# it is a hybrid sorting algorithim of  merge and insertion sort ''
"""

when array size is smaller it use insertion sort 
and when array is larger then it use merge sort 

"""


#----------------------
# kandane's Algorithm 
#----------------------

# a= [-4,-2,3,-1,-4,8,-2,3,-1,5,-6]

#it is use on array where we have to work with sub array 


# leetcode maximumsum of sub array
"""def maxArray(nums):
    currentSum=nums[0]
    maxSum=nums[0]
    for i in range(1,len(nums)):
        currentSum = max(currentSum+nums[i], nums[i])
        maxSum= max(currentSum,maxSum)

    return maxSum

a=[-4,-2,3,-1,-4,8,-2,3,-1,5,-6]
print(maxArray(a))"""


# leetcode maxproduct

def maxProduct(nums):
    minNum=nums[0]
    result=nums[0]
    maxNum=nums[0]
    for i in range(1,len(nums)):
        if nums[i]<0:
            temp=maxNum
            maxNum=minNum
            minNum=temp

        maxNum=max(nums[i],maxNum*nums[i])
        minNum=min(nums[i],minNum*nums[i])
        result=max(result,maxNum)
         
    return result
a=[1,-4,3,4,-5,-2,8]
print(maxProduct(a))