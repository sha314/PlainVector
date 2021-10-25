import math
import random
import utils

class Point:
    def __init__(self, pointA):
        self.coordinate = pointA
        self.dim = len(pointA)  # number of elements
        pass

    def distance_btn_points(self, pointB):
        distance = 0
        for i in range(self.dim):
            distance += (self.coordinate[i] - pointB.coordinate[i])**2
            pass
        return math.sqrt(distance)

    pass

def distance_btn_planes(self, planeA=(0, None, None), planeB=(10, None, None)):
    # planeA and planeB both are in yz plane

    pass


def coordinate_generate(mins:tuple=(0,0,), maxs:tuple=(20,20,)):
    # Integer coordinate generation
    # size of mins and maxs must be equal
    # their size determins the dimension of space

    xx = []
    for xmin, xmax in zip(mins, maxs):
        # xx.append(random.randint(xmin, xmax)*utils.sign())
        xx.append(random.randint(xmin, xmax) * (lambda: 1 if random.randint(0, 10) % 2 == 0 else -1)())
        pass
    return tuple(xx)



if __name__ == '__main__':
    print("Generate coordinate")
    print(coordinate_generate())
    print(coordinate_generate())
    print(coordinate_generate())
    print(coordinate_generate((0, 0, 0), (10, 10, 10)))



