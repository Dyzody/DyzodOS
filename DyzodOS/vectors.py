import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type. Vector2D can only be added to another Vector2D.")

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type. Vector2D can only be subtracted from another Vector2D.")

    def get_length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def showInText(self):
        return f"X:{self.x} Y:{self.y}"

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

def normalizeVector(Vector, length):
    current_magnitude = math.sqrt(Vector.x**2 + Vector.y**2)
        
    if current_magnitude == 0:
        return Vector2D(0, 0)
        
    scale_factor = length / current_magnitude
    normalized_x = Vector.x * scale_factor
    normalized_y = Vector.y * scale_factor
    normalized_vector = Vector2D(normalized_x, normalized_y)
    return normalized_vector

def getaverageVector(Vec1, Vec2):
    averageX = (Vec1.x + Vec2.x)/2
    averageY = (Vec1.y + Vec2.y)/2

    averageVector = Vector2D(averageX, averageY)
    return averageVector

def getSize(Vec):
    return Vec.x*Vec.y