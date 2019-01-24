#!/usr/bin/env python3

__author__ = 'liuyifan'
import math

# import matplotlib.pyplot as plt # Bonus No.1
# import math # Bonus No.2

def fx(equation,x):
    '''
    x:integral
    returns:(integral) f(x)
    '''
    return eval(equation.replace('x',str(x)))

class Integral:
    '''
    The Solution Class

        substitute the `pass` statements with your own code,
        you are allowed to define your own functions in order to keep your
        code clean

    Usage:
        In[1]:  Integral("2 * (x ** 3)", 0, 10)()
        Out[1]: 4999.99xx

        In[2]:  result = Integral("2 * (x ** 3)", 0, 10)
        In[3]:  result()
        Out[3]: 4999.99xx
    '''



    def __init__(self, equation, start, end,
                 default_step=1):
        '''
        Initialize the solution class

        Args:
            equation        - `eval()`-able string like
                              "2 * (x ** 3) - 4 * (x ** 0.5)", where `x` is
                              the placeholder
            start           - integral start
            end             - integral end
            default_step    - float

        Return:
            the integral value
        '''
        self._equation = equation
        self._start = start
        self._end = end
        self._default_step = default_step

        # test if equation is valid
        try:
            low = eval(equation.replace('x', 'start'))
            high = eval(equation.replace('x', 'end'))
            between = (end-start)/2
            n = 1
            result_new = between*(low+high)
            while 1:
                result_before = result_new
                i = 1
                g = 0
                for i in range(n+1):
                    temp = fx(equation,start+(2*i-1)*between)
                    g = g + temp
                result_new = float(result_before/2 + g*between)
                between = between/2
                n = n*2
                print ("result==>",result_new)
                if(math.fabs(result_new - result_before) < 0.01):
                    break

        except SyntaxError: # equation not valid
            print("Unsupported expression!")

    def __call__(self, *args, **kwargs):
        '''
        Do the calculation and return the value
        '''
        pass

# Testing
if __name__ == '__main__':
    equation = input("equation: ")  # get equation from user
    if 'x' in equation:
        # test run:
        # integral from 0 to 10 ( equation ) dx
        Integral(equation, 0, 10)()
    else:
        print ("result==>",(10-0)*eval(equation))
    print ("end")
