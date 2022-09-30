# Python Class Decorator

class MyDecorator(object):
    def __init__(self, func):
        self._func = func
        
    def __call__(self, name):
        print('Some decoration code')
        self._func(name)

def my_method(name):
    print('My name is {}'.format(name))
    
@MyDecorator
def my_method_decorated(name):
    print('My name is {}'.format(name))

if __name__ == '__main__':
    # Equivalent ways to represent decorator
    print(my_method_decorated('Peter'))
    print((MyDecorator(my_method))('Peter'))
