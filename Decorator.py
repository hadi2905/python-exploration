import datetime as dt
import math
import random

def mydeco(fnc):
    def wrapper(*args, **kwargs):   # Der Wrapper ist für beide Parameterarten bereit
        print("Wrapper für " + fnc.__name__)
        print("args=", args)
        print("*args=", *args)
        if kwargs != {}:
            print("kwargs=", kwargs)
            print("*kwargs=", *kwargs)
            print("kwargs['seed']=", kwargs['seed'])
        #print('z=',z)
        return fnc(*args, **kwargs)
        print('Hello2')
    return wrapper

@mydeco
def addition(arg1, arg2):       # nimmt zwei Positionsparameter
    n = arg1 + arg2
    return n

@mydeco
def zufall(wert, seed=0):       # nimmt einen Positions- und einen benannten Parameter
    random.seed(seed)
    print('so ein Zufall')
    return wert*random.random()

if __name__=='__main__':
    print(addition(5,16))
    print(zufall(99, seed=50))