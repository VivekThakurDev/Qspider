def singlenumber(num):
    res=0
    for n in num:
        res^=n
    return res
a=singlenumber([1,2,2,1,5])
print(a)
