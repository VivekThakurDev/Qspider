# '''
# Split function [ split() ]:-
#  1. it is used to split the string into list of string based on the given seper
#   split is a function of string whoch split the function of string with wide space and store the string into the list
# Syntax:-   var.split()


# For Loop :-
#  1. it is self iterative loop 
#  2. it will allow us to use all the multi value data type
#  3. no need of insilization and updation 
# '''
# '''
# Syntax :-
#          for var in collect:
#          <---1 TAB-->Statment Block

# '''
# '''
# Range():-
#             it is used  to create a sequence of integers between the given value.

#     Syntax:-        renge(SV,EV+1,UP)

# '''
# # list(range(1,11))

# # for a in [22,34,23,21]:
# #     print(a)



# ##   WAP to print all the integer present in a list
# '''
# l= eval(input('enter the list :- '))
# for a in l:
#     if type(a)== int:
#         print(a)
# '''


# ####   WAP to ectract all the even number present int a list 
# '''
# for a in [12,1.2,22,32,42]:

#     if a%2==0 :
#         print(a)

#         '''

# ####   WAP  to  remove dupilcate form the list 
# '''
# l= eval(input('enter the list:- '))
# h=[]
# for a in  l :
#     if a not in h:
#         h.append(a)
# print(h)
# '''

# ####  WAP to  reverse a string without slicing 

# n = input('Enter a string:- ')
# rev=''
# for i in n :
#     rev = i+rev 
# print(rev)




# ####  WAP to extract all the lowercase character from a string only if the asscii value is even  
# '''


# n =input('Enter a sting where is include lower and Upper case:- ')
# lc= []
# for i in n :
#     if  'a' <=i<='z' and ord(i)%2 == 0:
#         lc.append(i)
# print(lc)

# '''
 



# ####  Wap to extract key value pairs from the dictoinary onlyif both keys are of string datatype and values are integers
# '''
# d= { 'a':2,'b':3,True:33}
# for i in d:
#     if type(i)==str and type(d[i]) == int:
#         print(i,':',d[i])
# '''

# ### WAP to extract key value pairs from the dictionary only if both keys and values are exactly same.

# '''

# d= { 'a':2,'b':3,True:33,'c':'c','d':'d','E':'f'}
# out={}
# for i in d:
#     if i== d[i]:
#         out[i]=d[i]
# print(out)


# '''


# ###n  WAP to get the following output using len function 
# #                 s= 'power star'
# #                 out = {'power':5,'star':4}
# '''

# s= 'power star'.split()

# out = {}
# for i in s:
#     out[i]= len(i)
# print(out)

# '''

# ###  WAP to get th following output.
#     # s= 'power star'
#     # out= ('power':'rewop','star':'rats')
# '''
# s= 'power star'.split()
# out={}
# for i in s:
#     out[i]= s[::-1]
# print(out)
# '''
# ### WAP to replace the space by * present in a string 

# '''
# s= 'Hello World'
# out=''
# for i in s:
#     if i == ' ':
#         out+='*'
#     else:
#         out+=i
# print(out)

# '''

# ###   WAP to extra,ct all the non default values from a list.
# '''
# l = [ (),{},'int',25,'sds']
# out= []
# for i in l :
#     if bool(i)== True:
#         out.append(i)
# print(out)

# '''


# ###  WAP to count the number of  occurance of a specified  chararter.
# '''
# l='vivek'
# c='v'
# count=0
# for i in l:
#     if i == c:
#         count +=1
# print(count)

# '''




# ### WAP to count th number of occurance if charecter 

# '''
# l='amit'
# out={}
# count=0
# for i in l:
#     if i not in out:
#         out[i]=1
#     else:
#         out[i]+=1
# print(out)

# '''

# ### WAP to get the following output.
# #  In =' push maadi kushi padi'
# # out = { 'push':'ph', 'maadi:'a', 'kushi':'s','padi':'pi' }
# '''
# In ='push maadi kushi padi'
# out={}
# for i in In.split():
#     if len(i)%2==0:
#         out[i]= i[0]+i[-1]
#     else:
#         out[i]= i[len(i)//2]
# print(out)
# '''

# ##  WAP to get the following output.
#     #          s= 'always keep smiling'
# #             out = ' syawal pssk gnglims'
# '''
# s= 'always keep smiling'.split()
# out=''
# for i in s:
#     if i not in out:
#         rev= i[::-1]
#         out= out+rev+(' ')
# print(out.splitlines())


# '''

# ## WAP extract  upper , lower,digit. and special character present in a string to differnt output
#  #    .output variable

# # st = input('enter the charecter:- ')
# # uc=''
# # lc=''
# # sp=''
# # di=''
# # for i in st:



# # WAP to get the following output
# # s= ['jiocinema.com','file.py','web.html','amazon.com',vvv.org]
# '''
# ls=[]
# for i in s:
#      name,ex= i.split('.')
#      if name not in ls:
#           ls.append(ex)
# print(ls)
# '''
# #           OR
# '''
# s= ['jiocinema.com','file.py','web.html','amazon.com','vvv.org']
# ls=[]
# for i in s:
#     i= i.split('.')[-1]
#     if i not in ls:
#         ls.append(i)
# print(ls)

# '''

# ### WAP to get the following output
# #s= ['Jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
# #ut={'com': ['Jiocinema', 'amazon'], 'py': ['file', 'python'], 'html': ['web'], 'org': ['www']}
# '''

# s= ['Jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
# out={}
# for i in s:
#     i= i.split('.')
#     if i[1] not in out:
#         out[i[1]]= [i[0]]
#     else:
#         out[i[1]].append(i[0])
# print(out)

# '''


# ### WA{P to get the following output
# ##  L=['hai',34,3.4,'hello',90,'byebye']
# # out= {'hai':'hi','hello':'ho','byebye':'be'}

# '''
# L=['hai',34,3.4,'hello',90,'byebye']
# out ={}
# for i in L:
#     if type(i) == str:
#         out[i]= i[0]+ i[-1]

# print(out)
# '''


# #### WAP to get the following output

# '''
# In='hello'
# Out={0:'h',1:'e',2:'l',3:'l',4:'o'}
# In='hello'
# out={}
# '''

# # c=0
# # for i in In:
# #     out[c]=i
# #     c+=1
    
# # print(out)
#   ###              OR 
# '''
# for i in range(len(In)):
#      out[i]= In[i]
# print(out)
# '''  



# ###  WAP to extract all the string values present in the list only it he string is palindrom 
"""
s= [3,'mom',True,'hi',8.9,'appa']
t=[]
for i in s:
    if type(i) == str and i == i[::-1]:
        t.append(i)
print(t)

"""


# ##  WAP to  return the position of vowels present in the given string

# l = input('enter the string')
# dic=[]
# v=['A','E','I','O','U','a','e','i','o','u']
# for i in range(len(l)):
#      if i in v:
#           dic[i]=l[i]
# print(dic)





# s= ['jiocinam.com','vivek.py','alu.on']
# out=[]
# for i in s:
#     i=i.split('.')[-1]
#     if i not in out:
#         out.append(i)
# print(out)


## WAP to count the number of word in a string 
In= 'kslksl1232'
out=' '
for i in In:
    if '0'<=i<='9':
         out +=i
print(out)
        




