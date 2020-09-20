from main_py.constants import *
from main_py.vector import Vector
import math

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

def electricField_one_infinite_sheet(density_sigma):

    return density_sigma / (2. * epsilon_naught_full)

def electricField_one_infinite_sheet_vector(density_sigma, positionOfSheet, positionVectorAtP):

    pass

def electric_field_mag_rod_symmetry_axis(charge_q, r_source_to_point, rod_length):
    a = coulomb_constant_full*charge_q / r_source_to_point
    b = math.sqrt(r_source_to_point**2 + (rod_length/2)**2)
    return a / b
    pass

def test():
    print("test : ", __file__)
    charge = charge_of_electron_full
    distance = 5. # in meters
    print(electricField(charge, distance))

    distance = Vector([5, 0, 0])  # in meters
    print(electricField(charge, distance))