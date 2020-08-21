

def series_resistance(R1, R2, order=1):
    return (R1 + R2) * order


def parallel_resistance(R1, R2, order=1):
    return R1*R2*order/(R1 + R2)
