#-----------------
#Abstraction 
#------------------

'''
-> it is the fundamental of opps where be hide the implementation to hide the functionality.
-> we have three type of abtraction 
1) Abstraction method
2) Abstraction class 
3) concrite class 
'''
#-------------------
# Abstract method 
#-------------------
'''
it is athe method where we call the decorator abstract method by importing import ABC
'''
"""

from abc import ABC ,abstractmethod
@abstractmethod
class c_name(ABC):
    def m_name(arg):
        pass

from abc import ABC,abstractmethod
class c_name(ABC):
    @abstractmethod
    def m_name(arg):
        pass"""


# Example 2
"""
from abc import ABC,abstractmethod
class train(ABC):
    @abstractmethod
    def seat1():
        pass
    @abstractmethod
    def seat2():
        pass


class c_train():
        def seat1():
             print('my seat')

        def seat2():
             print('other seat')

obj1=c_train()
print(c_train.seat1())
print(c_train.seat2())

"""

