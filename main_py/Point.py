import math

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