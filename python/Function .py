# it is a  name given to a memory block where the set of instructions are store and 
# that instruction perform some specific task 


## Why we need function.
# we can reduce the number of instructions.
# we an increase the efficency of the code.
# we can avoid code repetition.
# we can reuse the coe for n number if times.


## Types of function
# 1.inbuild function:-   we can access them but cannot modify there orginal task
# 2.user-defined function

##################### In Build Function####################################
# these are pre-defined function.
# 1)  Utility function
# 2)  funtion on string
# 3)  function on list
# 4)  function on tuple 
# 5)  function on set
# 6)  function on dict

# 1)  Utility function:-
#the function that we use or apply on every data type
"""that are:- 
bool()
print()
type()
id()
"""

# FUNCTION ON STRING:
# these are the function which is apply in string data type 
# upper():- it will convert all lower case character to upper case 
#              Syntax:-  var.upper()
# lower():- it will convert all the character into lower case
#               Syntax:-  var.lower()
# swapcase():-  it will convert the lower case into upper case and upper cse into lower case
#                 Syntax:-   var.swapcase()


# capitalize():-  it will convert the first letter into upper case of the in the string
#                 Syntax :-  var.capitalize()   Example- 



# split():-  it is use to split the string according to space, point, comma  or in the base on charecter 
#           and to store in list 
#             Syntax:- var.split()
#             Example:- 'Function on string'
#                       >>> f.split('o')
#                           ['functi', 'n ', 'n string']

#  replace():-  it will replace the charecter from the string 
#                Syntax:-        var.replace('old_Char','new_char')

#    count():-    it will count the occurance of cahracter
#                 syntax:- var.count()

#  ord():-  it will use to find out theparticular  ACII value of the number 
#                ord('char')


 # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

 # FUNCTION ON LIST:- 
 # append():- 
 # pop()
 # remove()
 # insert() 
 #  extend():- 
 #          syntax:-   var.extend([val1,val2,......val_n])
 #                      >>> l=[1,2,54,5,3,5,4]
#                       >>> l.extend([8,9,7])
#                       >>> l =[1, 2, 54, 5, 3, 5, 4, 8, 9, 7]
# sort():- it is use to short he data  of list in accending order
#               syntax:- var.sort()
#     for decending order:-   var.sort(reverse=True)

# reverse():- it is use to reverse the data of the list 
#           syntax:-  var.reverse()

# count():- it will the count the element of the list 
#           syntax:- var.count()

# index():- 
#        syntax:- var.index()




#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# FUNCTION OF TUPLE:- 
# index()
#           var.index(value)
# count()
#           var.count(value)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# FUNCTION OF SET 
# union():-it wil merge the two sets
#                    var1.union(var2)

#  intersection(): it will return only element from both the sets.
#                 syntax:- var1.intersection(var2)

#   difference(): it wil return unique element from set 1
#                syntax:- var1.difference(var2) 

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#  FUNCTION ON DICT
#  pop():- it will remove the element from the dictionary
#            syntax:-  var.pop(key)

#  get():- 
#        syntax:-  var.get(key)
#  popitem():- 
#          syntax:-  var.popitem()
#  update:- upadte the value of the dictionary
#             var.update(dict)

