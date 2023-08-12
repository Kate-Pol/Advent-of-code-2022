def read_lines():
    with open("day_9.txt") as f:
        return f.read().splitlines()
    

class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, 
                      self.y + other.y)
        
    def __sub__(self, other):
        return Vector(self.x - other.x, 
                      self.y - other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})" 
    
