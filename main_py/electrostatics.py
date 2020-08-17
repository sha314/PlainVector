from main_py.constants import *
from main_py.vector import Vector


def electricField(chargeQ, vectorFromOrigin):
    tempa = coulomb_constant_full * chargeQ
    try:
        a = float(vectorFromOrigin)
        return tempa / vectorFromOrigin**2
    except:
        print("vectorFromOrigin is a Vector Object")
        norm = vectorFromOrigin.norm()
        tempb = vectorFromOrigin / norm**3
        return tempa * tempb


def test():
    print("test : ", __file__)
    charge = charge_of_electron_full
    distance = 5. # in meters
    print(electricField(charge, distance))

    distance = Vector([5, 0, 0])  # in meters
    print(electricField(charge, distance))