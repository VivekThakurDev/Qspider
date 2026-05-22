# WAP to get the following output .without length function 
# s= 'power star'
# out = {'power':5,'star':4}

"""s= 'power star'.split()
out = {}
for i in s:
    count = 0
    for j in i:
        count+=1
    out[i]= count
print(out)"""


## WAP to get the following output
"""
s='hai hello '
out={'hai':'ai','hello':'eo'}

s= s.split()
out={}
for i in s:
    vo=''
    for j in i:
        if j in 'aeiouAEIOU':
            vo+=j
    out[i]=vo
print(out)
"""
##WAP to
# s= 'power star'
#  out ={power:2,star:1}
"""s= 'power star'.split()
out={}
for i in s:
    count = 0
    for j in i:
        if j in 'aeiouAEIOU':
            count+=1
    out[i]= count
print(out)"""

## WAP to get the following output .
#  s= 'kabab is love'
# out={'kb':(''kbb',3,bbk),'is':('s','l','s'),'le': ('lv',2,'vl')}
# {1st+last char:(consonant,no of consonanat,rev of consonant)}

# s= 'kabab is love'
# s= s.split()
# out={}
# for i in s:
#     con=''
#     for j in i:
#         if j not in 'aeiouAEIOU':
#             con+=j
#     out[i]=(con, len(con), con[::-1])
# print(out)

# or 

"""s= 'kabab is love'.split()
out={}
for i in s:
    vo = 0
    ind=''
    for j in range(len(i)):
        if i[j]  in 'aeiouAEIOU':
            vo+=1
        if j%2 ==0:
            ind+=i[j]
    out[i]=(ind[::-1],vo,ind)
print(out)"""

#  WAP to get the following otput.
#In =[100,200,35,40,60]
#out=[335,235,400,395,375]    (total sum-val)
"""
In=[100,200,35,40,60]
out=[]
for i in In:
    total =0
    for j in In:
        if i!=j:
            total+=j 
    out.append(total)
print(out)
"""
## WAP to get the following output
#        In='bacbcaabbaa'
#         Out='b4a5c2'
"""In='bacbcaabbaa'
out=''
for i in In:
    count = 0
    for j in In:
        if i==j:
            count+=1
    if i not in out:
        out+=i+str(count)
print(out)"""


## WAP to get the following output
#  In = [100,200,50,400,300,150,125,175]
#  N=300
#  Out =[100,200],[300],[150,150],[125,175]
# In = [100,200,50,400,300,150,125,175]   

  
In = [100,200,50,400,300,150,125,175]
N=300
out=[]
"""for i in range(len(In)):
    for j in range(i, len(In)):
         if In[i] == N:
                out.append([In[i]])
                break
         elif In[i]+In[j] == N:
                out.append([In[i],In[j]])       
print(out)"""
#or



##  WAP to get tye following output
#  In={10:'star',20:'bye',30:'moon',40:'apple'}
#  Out=(10:'a',20:'e',30:'oo',40:'ae')

"""
In={10:'star',20:'bye',30:'moon',40:'apple'}
out={}
for i in In:
    vowels=''
    for j in In[i]:
        if j in 'aeiouAEIOU':
            vowels+=j
    out[i]=vowels
print(out)

"""

# WAP to get the following output
#  In= ['hello',227,'last',3.4,189,34]
# out= [722,981,43]
"""
n= ['hello',227,'last',3.4,189,34]
out=[]
for i in n:
    if type(i)== int:
        n= str(i)[::-1]
        out.append(n)
print(out)
         
"""
# or 
"""
n= ['hello',227,'last',3.4,189,34]
out=[]
for i in n:
    if type(i)== int:
        rev=0
        while i !=0:
            Id = i % 10
            rev = rev*10 + Id
            i = i // 10
        out.append(rev)
print(out)  
"""