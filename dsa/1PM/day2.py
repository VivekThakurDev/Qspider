#----------------------------
# facinatting number 
#----------------------------
"""
def fascinating_number(num):
    s= str(num)+str(num*2)+str(num*3)
    freq=[0]*10
    for digit in s:
        freq[int(digit)]+=1
    if len(s)==9 and all(count==1 for count in freq[1:]):
        return True
    return False
print(fascinating_number(194))
"""


# Majority element  in array 

def majorityelement(nums):
    count={}
    for n in nums:
        count[n]= count.get(n,0)+1
    majority_count=len(nums)//2
    for num,freq in count.items():
        if freq > majority_count:
            return num
    

print(majorityelement([1,2,3,2,2,5,4,2]))