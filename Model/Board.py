from random import shuffle

class Board:
    def __init__(self):
        numberFiches = [x for i in range(2,13) for x in [i]*3]
        shuffle(numberFiches)
        self.tileList = [self.Tile(numberFiches[i]) for i in range(19)]
        

    def __str__(self):
        s="Board:"
        s+=' '.join(str(tile) for tile in self.tileList)
        
        return s

    

    class Tile:
        def __init__(self,value):
            self.value = value


        def __str__(self):
            return f"Tile: {self.value}"

