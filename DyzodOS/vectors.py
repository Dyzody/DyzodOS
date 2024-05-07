import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        if isinstance(other, Vector2D):
            return self.get_length() < other.get_length()
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Vector2D):
            return self.get_length() > other.get_length()
        return NotImplemented

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def vectorclamp(self, Vector):
        if Vector.x > 0:
            if self.x > Vector.x:
                self.x = Vector.x
        else:
            if self.x < Vector.x:
                self.x = Vector.x
        if Vector.y > 0:
            if self.y > Vector.y:
                self.y = Vector.y
        else:
            if self.y < Vector.y:
                self.y = Vector.y
    
    def InText(self):
        return f"X:{self.x} Y:{self.y}"


def normalizeVector(Vector, length):
    
    if not isinstance(Vector, Vector2D): 
        return NotImplemented

    current_magnitude = Vector.get_length()
        
    if current_magnitude == 0:
        return Vector2D(0, 0)
        
    scale_factor = length / current_magnitude
    normalized_x = Vector.x * scale_factor
    normalized_y = Vector.y * scale_factor
    normalized_vector = Vector2D(normalized_x, normalized_y)
    return normalized_vector

def getaverageVector(Vec1, Vec2):
    
    if not isinstance(Vec1, Vector2D) or not isinstance(Vec2, Vector2D): 
        return NotImplemented
    
    averageX = (Vec1.x + Vec2.x)/2
    averageY = (Vec1.y + Vec2.y)/2

    averageVector = Vector2D(averageX, averageY)
    return averageVector

def getSize(Vec):
    return Vec.x*Vec.y