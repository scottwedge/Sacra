class matrix3d:
    """ Intalizes a matrix which is in R^3 space; Of which the basic eigen-values can be computed. """
    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        self.matrix = (self.vec1, self.vec2, self.vec3)

    def __str__(self):
        return f'<({self.vec1[0]}, {self.vec1[1]}, {self.vec1[2]})\n ({self.vec2[0]}, {self.vec2[1]}, {self.vec2[2]})\n ({self.vec3[0]}, {self.vec3[1]}, {self.vec3[2]})>'

    def __add__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __radd__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __rsub__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return matrix3d(vec1 * other, vec2 * other, vec3 * other)
        elif isinstance(other, vec3d):
            col1 = self.vec1[0] * other[0] + self.vec1[1] * other[1] + self.vec1[2] * other[2]
            col2 = self.vec2[0] * other[0] + self.vec2[1] * other[1] + self.vec2[2] * other[2]
            col3 = self.vec3[0] * other[0] + self.vec3[1] * other[1] + self.vec3[2] * other[2]
            return vec3d(col1, col2, col3)
        elif isinstance(other, matrix3d):
            x1 = self.vec1[0] * other.vec1[0] + self.vec1[1] * other.vec2[0] + self.vec1[2] * other.vec3[0]
            x2 = self.vec1[0] * other.vec1[1] + self.vec1[1] * other.vec2[1] + self.vec1[2] * other.vec3[1]
            x3 = self.vec1[0] * other.vec1[2] + self.vec1[1] * other.vec2[2] + self.vec1[2] * other.vec3[2]
            nvec1 = vec3d(x1, x2, x3)
            y1 = self.vec2[0] * other.vec1[0] + self.vec2[1] * other.vec2[0] + self.vec2[2] * other.vec3[0]
            y2 = self.vec2[0] * other.vec1[1] + self.vec2[1] * other.vec2[1] + self.vec2[2] * other.vec3[1]
            y3 = self.vec2[0] * other.vec1[2] + self.vec2[1] * other.vec2[2] + self.vec2[2] * other.vec3[2]
            nvec2 = vec3d(y1, y2, y3)
            z1 = self.vec3[0] * other.vec1[0] + self.vec3[1] * other.vec2[0] + self.vec3[2] * other.vec3[0]
            z2 = self.vec3[0] * other.vec1[1] + self.vec3[1] * other.vec2[1] + self.vec3[2] * other.vec3[1]
            z3 = self.vec3[0] * other.vec1[2] + self.vec3[1] * other.vec2[2] + self.vec3[2] * other.vec3[2]
            nvec3 = vec3d(z1, z2, z3)
            return matrix3d(nvec1, nvec2, nvec3)
        else:
            pass

    def trace(self):
        return self.vec1[0] + self.vec2[1] + self.vec3[2]




class vec3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (self.x, self.y, self.z)

    def __str__(self):
        return f'<({self.x}, {self.y}, {self.z})>'

    def __add__(self, other):
        if isinstance(other, vec3d):
            return vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __radd__(self, other):
        if isinstance(other, vec3d):
            return vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, vec3d):
            return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __rsub__(self, other):
        if isinstance(other, vec3d):
            return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __mul__(self, value):
        if isinstance(value, vec3d):
            pass
        else:
            return vec3d(self.x * value, self.y * value, self.z * value)

    def __rmul__(self, value):
        if isinstance(value, vec3d):
            pass
        else:
            return vec3d(self.x * value, self.y * value, self.z * value)

    def __getitem__(self, index):
        return self.vector[index]

    def dot(self, other):
        if isinstance(other, vec3d):
            value = self.x * other.x + self.y * other.y + self.z * other.z
            return value
        else:
            pass

    def cross(self, other):
        if isinstance(other, vec3d):
            col1 = self.y * other.z - self.z * other.y
            col2 = self.z * other.x - self.x * other.z
            col3 = self.x * other.y - self.y * other.z
            return vec3d(col1, col2, col3)
        else:
            pass

    def norm(self):
        value = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)
        return value

    def normalize(self):
        return 1 / (self.norm()) * self




class Object:
    def __init__(self, vec, offset):
        self.vec = vec
        self.offset = offset

    def __str__(self):
        return f'Solid object'

vec1 = vec3d(1, 1, 1)
object1 = Object(vec1, 1)
print(object1)
