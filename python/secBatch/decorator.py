#-------------
# Decorator
#-------------
"""
it is a function which is use to add extra functonaltiy to the main function 
without  modifying the main function

# it is function which takes another function as input.
"""

# there are two type of decorator:
"""
  1  prebuilt decorator /Inbuilt Decorator
     Example :-  class method , static method ,property 
 
   2  user define decorator 
     -> 
"""
# how to create a decorator 
"""
  --->  def decorator_name(func):
               def wrapper(*args,**wargs):
                    ------------
                    | pre task |
                     ----------
                    function (*args,**wargs)
                    ---------------
                    | Post task   |
                     --------------
                return wrapper
"""

# How to use decorator
"""

@decorator_name
def main_function(args):
    -----------
    |    SB    |
    -----------

 """                          
#  How to decorator is called 
"""

main_func = decorator_name(main_func)
"""
# 

# Example:-

def instagram(func):
    def wrapper(*args,**kwargs):
        print('Go to www.instagram.com')
        print(f" {args[0]} login successfully")    #  watch again and try to solve this 
        func(*args,**kwargs)
        print('logout')
    return wrapper

@instagram 
def vivek_insta(name):
    print('post story')
    vivek_insta('vivek')
@instagram
def goda_insta():
    print('chatting kiya')
@instagram
def susi_insta():
    print('watch reel')


# vivek_insta()
# print('-'*30)
 
# goda_insta()
# print("-"*20)

# susi_insta()
# print("-"*30)

vivek_insta= instagram(vivek_insta)
print(vivek_insta())