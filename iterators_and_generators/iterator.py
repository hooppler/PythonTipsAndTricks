# Python Itterator and Itterable

class MyIterator:
    def __iter__(self):
        self.itr = 0
        return self
        
    def __next__(self):
        x = self.itr
        self.itr += 1
        return x

if __name__ == '__main__':
    my_iterable = MyIterator()
    # iter() and __iter__() are the same methods
    # iterator = my_iterable.__iter__()
    iterator = iter(my_iterable)
    
    # next() and __next__() are the same methods
    # print(iterator.__next__())
    # print(iterator.__next__())
    # print(iterator.__next__())
    
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    
