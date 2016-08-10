class Fruit(object):

    def __init__( self, vit, weight):
        self.vitamins = vit
        self.weight = weight
        self._freshness = 100
        self._sourness = 1
        self._sweetness = 1
        self._bitterness = 1

    def rot(self):
        self._freshness -= 1
        
    def is_rotten():
        return self._freshness <= 0

    def get_taste(self):
        return ( self._sweetness,
                 self._sourness,
                 self._bitterness )

                 
class Apple(Fruit):
    
    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self._sourness = 5
        self._sweetness = 20
        self._bitterness = 2
    
    def rot(self):
        self._freshness -= 4


class Lemon(Fruit):
    
    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self._sourness = 20
        self._sweetness = 2
        self._bitterness = 5
    
    def rot(self):
        self._bitterness += 1
        self._freshness -= 2
