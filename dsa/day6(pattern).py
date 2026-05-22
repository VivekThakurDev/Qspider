# def print_pattern(n):
#     num=64+1
#     patternwidth= 1
#     space=n-1
#     for i in range(1,n+1):
#         for j in range(1,space+1):
#             print(' ',end='\t')
#         for j in range(1,patternwidth+1):
#             print(chr(num),end='\t')
#             num-=1
        
#         space=space-1
#         patternwidth=patternwidth+2
#         num+=2*i+1
#         print()
# print_pattern(5)            
'''
PS D:\QSpider\dsa> python -u "d:\QSpider\dsa\day6(pattern).py"
                                1
                        3       2       1
                5       4       3       2       1
        7       6       5       4       3       2       1
9       8       7       6       5       4       3       2       1
'''


# def print_pattern(n):
#     patternwidth=1
#     num= n*(n+1)//2+64
#     space=1
#     for i in range(1,n+1):
#         for j in range(1,space+1):
#            print(' ',end='\t')
#         for j in range(1,patternwidth+1):
#             print(chr(num),end='\t')
#             num+=1

#         space=space-1
#         patternwidth=patternwidth+2
#         num=num-2*i+1
#         print()
        
# print_pattern(5)

def printPattern(n):
    patternwidth=1
    num=64+1
    space=n-1
    for i in range(1,n+1):
        for j in range(1,space+1):
            print("  ",end='\t')
        for j in range(1,patternwidth+1):
            print(chr(num),end='\t')
            num-=1
        space-=1
        patternwidth+=1
        num+=2*i+1
        print()
n=3
printPattern(n) 