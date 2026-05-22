
def smallnumbercounterthancurrent(nums):
    freq=[]
    for n in nums:
        freq[n]+=1
    for i in range(1,100):
        freq[i]=freq[i]+freq[i-1]
    
    for  i in range(0,str(len(nums))):
        if nums[i]==0:
            

