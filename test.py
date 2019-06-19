# -*- coding: utf-8 -*-
import pdb
def test_var_args(f_arg, *argv):
    print u'Первый аргумент это -> ', f_arg
    for arg in argv:
        print u'Это другой аргумент: ', arg
test_var_args(1, 2,3,4,5,6)

def sum_of_args(*argv):
    sum_of_args = 0
    for arg in argv:
        sum_of_args += arg
    return sum_of_args

print sum_of_args(1,2)
print sum_of_args(4,6,78)
print sum_of_args(12,0)

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="Evgeniy", family="Danilov", age="31")

def test_args_kwargs(arg1, arg2, arg3):
    print u'arg1: ', arg1
    print u'arg2: ', arg2
    print u'arg3: ', arg3

args = (u'two', 3, 5)
test_args_kwargs(*args)

pdb.set_trace()
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

print test_args_kwargs.__name__
print ("Add new row for test git")