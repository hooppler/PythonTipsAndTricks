# Python Function Decorator

def my_decorator(func):
    def wraper(*arg, **kwarg):
        print('Some decoration code before method')
        result = func(*arg)
        print('Some decoration code after method')
        return 'Decorated result: {}'.format(result)
        
    return wraper


def my_method(name):
    result = 'My name is {}'.format(name)
    print(result)
    return result
    
@my_decorator
def my_method_decorated(name):
    result = 'My name is {}'.format(name)
    print(result)
    return result
    

if __name__=='__main__':
    # Equivalent ways to represent function decorator
    
    # Call method my_method decorated with decorator method my_decorator 
    # without using sintatical sugar @my_decorator
    print(my_decorator(my_method)('Peter'))
    
    # Call method my_method_decorated decorated with my_decorator
    # with useing sintatical sugar @my_decorator
    print(my_method_decorated('Peter'))
    


