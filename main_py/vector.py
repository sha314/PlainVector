import math

def levi_civita(i, j, k):
    return (i-j)*(j-k)*(k-i)/2

class Vector:
    def __init__(self, vec_a):
        self.vec = vec_a
        self.len = len(vec_a)
        pass

    def __add__(self, other):
        if self.len != other.len:
            print("cannot add vectors of different length")
            return None
        vec_c = []
        for i in range(self.len):
            vec_c.append(self.vec[i] + other.vec[i])
            pass
        return Vector(vec_c)

    def __sub__(self, other):
        if self.len != other.len:
            print("cannot add vectors of different length")
            return None
        vec_c = []
        for i in range(self.len):
            vec_c.append(self.vec[i] - other.vec[i])
            pass
        return Vector(vec_c)

    def __mul__(self, number):
        try:
            a = int(number)
        except:
            print("multiplication with a scaler is defined only")
            return None

        vec_c = []
        for i in range(self.len):
            vec_c.append(self.vec[i] * number)
            pass
        return Vector(vec_c)

    def __iadd__(self, other):

        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, number):
        return self.__mul__(number)

    def __imul__(self, number):
        return self.__mul__(number)

    def __truediv__(self, number):
        return self.__mul__(1.0 / number)

    def __rdiv__(self, number):
        return self.__truediv__(number)

    def __idiv__(self, number):
        return self.__truediv__(number)


    def __pow__(self, number):
        try:
            a = int(number)
        except:
            print("multiplication with a scaler is defined only")
            return None

        vec_c = []
        for i in range(self.len):
            vec_c.append(self.vec[i] ** number)
            pass
        return Vector(vec_c)

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        if index >= self.len:
            print("Out of range")
            return None
        return self.vec[index]

    def __setitem__(self, index, value):
        if index >= self.len:
            print("Out of range")
            return None
        self.vec[index] = value

    def __str__(self):
        string = "{}".format(self.vec)
        return string

    def dot(self, other):
        """
        dot product
        :param other:
        :return:
        """
        if self.len != other.len:
            print("cannot add vectors of different length")
            return None
        sum_vec = 0
        for i in range(self.len):
            sum_vec += self.vec[i] * other.vec[i]
            pass
        return sum_vec

    @staticmethod
    def dotProduct(vec1, vec2):

        pass

    @staticmethod
    def crossProduct(vec1, vec2):
        vec3 = [0]*3
        vec3[0] = vec1[1] * vec2[2] - vec2[1] * vec1[2]
        vec3[1] =-vec1[0] * vec2[2] + vec2[0] * vec1[2]
        vec3[2] = vec1[0] * vec2[1] - vec2[0] * vec1[1]
        return Vector(vec3)

    @staticmethod
    def crossProduct_v2(vec1, vec2):
        vec3 = [0] * 3
        for i in range(len(vec3)):
            for j in range(len(vec1)):
                for k in range(len(vec2)):
                    eps = levi_civita(i+1, j+1, k+1)
                    # print(eps)
                    vec3[i] += eps*vec1[j]*vec2[k]
                    pass
                pass
            pass
        return Vector(vec3)

    def norm(self):
        sum_of_squared = 0
        for elm in self.vec:
            sum_of_squared += elm ** 2
            pass
        return math.sqrt(sum_of_squared)

    def unitVector(self):
        length = self.norm()
        return self.__mul__(1/length)

    @staticmethod
    def vectors_from_points(point1, point2):
        """
        from point 1 to point 2
        """
        vec1 = Vector(point1)
        vec2 = Vector(point2)
        return vec2 - vec1

    def apply(self, func):
        out_vec = []
        for elm in self.vec:
            out_vec.append(func(elm))
            pass
        return Vector(out_vec)

    def toList(self):
        return self.vec

def test():
    vec1 = Vector([3, 4])
    vec2 = Vector([4, 3])
    print("vec1 ", vec1)
    print("vec2 ", vec2)
    print(vec1.norm())
    print(vec2.norm())
    print(vec1.unitVector())
    print("addition *************")
    vec3 = vec1 + vec2
    print(vec3)
    vec3 = vec2 + vec1
    print(vec3)
    vec3 = vec1
    vec3 += vec2
    print(vec3)

    vec3 = vec1 - vec2
    print(vec3)
    vec3 = vec2 - vec1
    print(vec3)
    vec3 = vec1
    vec3 -= vec2
    print(vec3)

    print("multiplication ********* ")
    print(vec1 * 2)
    print(2 * vec1)
    vec3 = vec1
    vec3 *= 2
    print(vec3)
    print(vec1 / 2.)

    print("dot product  ******* ***")
    vec3 = vec1
    print(vec3.dot(vec2))


    print("indexing ")
    print("x component ", vec1[0])
    print("y component ", vec1[1])
    print("z component ", vec1[2])

    print("cross product")
    vec1 = Vector([1, -2, 3])
    vec2 = Vector([-1, 3, -2])
    print("vec 1 ", vec1)
    print("vec 2 ", vec2)
    vec3 = Vector.crossProduct(vec1, vec2)
    print("vec 3 ", vec3)
    vec3 = Vector.crossProduct_v2(vec1, vec2)
    print("vec 3 ", vec3)
