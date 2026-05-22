#leetcode
"""
# Linear search
def mysqrt(x):
    for i in range(1,x):
        if i*i>x:
            return i-1
print(mysqrt(8))

"""

# Binary Search
"""def mysort(x):
    start=1
    end=x/2
    while start<=end:
        mid=start+(end-start)//2
        if mid*mid==x:
            return mid
        elif mid*mid > x:
            end = mid-1 
        else:
            start= mid+1
    return end
print(mysort(8))
        
"""

# minimum rotate array


def minimumrotate(x):
    start=0
    end=len(x)-1
    
    while start<end:
        mid = start+(end-start)//2
        if x[mid]>x[end]:
            start=mid+1
        elif:
            end=mid
    return f'Minimum element is: {x[start]}'
input=[12,5,24,12,4,2,5,4,12,48]
print(minimumrotate(input))