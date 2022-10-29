# Abstract class

from abc import ABC, abstractmethod


class Fruit(ABC):
    
    @abstractmethod
    def color(self):
        pass
        
        
class Banana(Fruit):
    pass
        
        
class Apple(Fruit):
    
    def color(self):
        return 'Red'
        
        
if __name__ == '__main__':
    #fruit = Fruit() # Will fail because abstract class cannot be instantiated
    #banana = Banana() # Will fail because abstract methods must be overriden
    apple = Apple() # Will be instantiated corectly
    
        


