from main_py.constants import *


def series_capacitance(C1, C2, order=1.):
    return C1*C2*order/(C1 + C2)


def parallel_capacitance(C1, C2, order=1.):
    return (C1 + C2) * order


def capacitance_parallel_plate(area_of_the_plates, separation_btn_plates):
    return epsilon_naught_full * area_of_the_plates / separation_btn_plates