# Python Decorators

def my_decorator(func):
    def wraper(*arg, **kwarg):
        print('Some decoration code')
        func(*arg)
        
    return wraper


def my_method(name):
    print('My name is {}'.format(name))
    
@my_decorator
def my_method_decorated(name):
    print('My name is {}'.format(name))
    

if __name__=='__main__':
    my_decorator(my_method)('Peter')
    my_method_decorated('Peter')
    


