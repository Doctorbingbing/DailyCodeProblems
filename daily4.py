#Given Implementation of cons
def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair
#cons pairs two numbers, impliment car and cdr to return the first and last elements of the pair respectively.
#cons returns a function named pair which itself takes a function

def cdr(pair):
    return pair(lambda a, b:b)
#If cdr, call pair on a lambda with pair a,b and return the second

def car(pair):
    return pair(lambda a, b:b)
#If car, call pair on a lambda with pair a,b and return the first
cdr(cons(4,5))
car(cons(4,5))