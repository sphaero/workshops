#!/usr/bin/python3
from random import randint


class TasteError(Exception):
    pass
    

class RottenError(Exception):
    
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error


class TastyMixin(object):
    """
    This class provides taste comparison operators
    """
    @staticmethod
    def total_taste(fruit):
        taste = fruit._sourness + fruit._sweetness + fruit._bitterness
        if taste > 25:
            raise TasteError("taste explosion {0}".format(taste))
        return taste
    
    def __lt__(self, other):
        st = self._sourness + self._sweetness + self._bitterness
        ot = other._sourness + other._sweetness + other._bitterness
        return self.total_taste(self) < self.total_taste(other)

    def __le__(self, other):
        st = self._sourness + self._sweetness + self._bitterness
        ot = other._sourness + other._sweetness + other._bitterness
        return st <= ot

    def __eq__(self, other):
        st = self._sourness + self._sweetness + self._bitterness
        ot = other._sourness + other._sweetness + other._bitterness
        return st == ot

    def __ne__(self, other):
        st = self._sourness + self._sweetness + self._bitterness
        ot = other._sourness + other._sweetness + other._bitterness
        return st != ot
    
    def __gt__(self, other):
        st = self._sourness + self._sweetness + self._bitterness
        ot = other._sourness + other._sweetness + other._bitterness
        return st > ot

    def __ge__(self, other):
        st = self._sourness + self._sweetness + self._bitterness
        ot = other._sourness + other._sweetness + other._bitterness
        return st >= ot


class Fruit(TastyMixin):

    def __init__( self, vit, weight):
        self.vitamins = vit
        self.weight = weight
        self._freshness = 100
        self._sourness = 1
        self._sweetness = 1
        self._bitterness = 1

    def rot(self):
        self._freshness -= 1
        if self._freshness < 1:
            raise RottenError("Fruit {0} has rotten".format(self), self._freshness)
        
    def is_rotten(self):
        return self._freshness <= 0

    def get_taste(self):
        return ( self._sweetness,
                 self._sourness,
                 self._bitterness )
    
    def __repr__(self):
        return "{0}({1},{2})".format(self.__class__.__name__, self.vitamins, self.weight)

    def __str__(self):
        return "{0} with {1} vitamins weighing {2}".format(self.__class__.__name__, self.vitamins, self.weight)

    def __add__(self, other):
        self._sourness += other._sourness
        self._sweetness += other._sweetness
        self._bitterness += other._bitterness


class Apple(Fruit):
    
    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self._sourness = 5
        self._sweetness = 20
        self._bitterness = 2
    
    def rot(self):
        self._freshness -= 4
        super().rot()


class Lemon(Fruit):
    
    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self._sourness = 20
        self._sweetness = 2
        self._bitterness = 5
    
    def rot(self):
        self._bitterness += 1
        self._freshness -= 2
        super().rot()


class Nature(object):

    def __init__(self, fruits):
        self.fruits = fruits
    
    def decay(self):
        to_delete = []
        for fruit in self.fruits:
            fruit.rot()
            if fruit.is_rotten():
                to_delete.append(fruit)
                
        for fruit in to_delete:
            print("Fruit {0} has rotten".format(fruit))
            self.fruits.remove(fruit)
                
    def run(self):
        while len(self.fruits):
            self.decay()


fruits = [ Apple(20+randint(0,4),20+randint(0,5)) for x in range(20) ]
for x in range(20):
    fruits.append( Lemon( 30+randint(0,3), 10+randint(0,3) ) )

Nature(fruits).run()

a = Apple(20,20)
l = Lemon(10,10)
a+l
print(a>l)
print(a<l)
