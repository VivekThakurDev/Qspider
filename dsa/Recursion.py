#if a method call itself then uit is called recursion. It is a programming technique in which a function calls itself in order to solve a problem. A recursive function typically has two main components: a base case that stops the recursion, and a recursive case that breaks the problem into smaller subproblems and calls itself to solve those subproblems.
#if it is not control then it cause stack OverflowError

#We can achive the recurion in three method 
'''
1. Direct Recursion
2. Indirect Recursion
3. Tail Recursion
'''
"""
1>  By calling method itself is called direct recursion
2>  by calling from another argument is called indirect recursion
2> By calling from return statment is called tail recursion

"""
##    1. Direct Recursion


def printNum(n):
    print(n)
    print(n+1)
printNum(1)