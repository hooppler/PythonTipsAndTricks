# Python Class Decorator

class MyDecorator(object):
    def __init__(self, func):
        self._func = func
        
    def __call__(self, name):
        print('Some decoration code before method')
        result = self._func(name)
        print('Some decoration code after method')
        return 'Decorated result: {}'.format(result)

def my_method(name):
    result = 'My name is {}'.format(name)
    print(result)
    return result
    
@MyDecorator
def my_method_decorated(name):
    result = 'My name is {}'.format(name)
    print(result)
    return result
    

if __name__ == '__main__':
    # Equivalent ways to represent class decorator
    
    # Call method my_method decorated with decorator class MyDecorator 
    # without using sintatical sugar @MyDecorator
    print((MyDecorator(my_method))('Peter'))
    
    # Call method my_method_decorated decorated with MyDecorator
    # with useing sintatical sugar @MyDecorator
    print(my_method_decorated('Peter'))



