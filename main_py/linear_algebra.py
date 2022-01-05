from main_py import vector
import sys

Vector = vector.Vector

class LinearAlg:
    """
    Linear Algebra class
    """

    @staticmethod
    def choose_pivot(eqn):
        """
        pivot is the first non zero element of an equation
        :param eqn:
        :return: index and value of pivot
        """
        for i in range(len(eqn)):
            b = eqn[i]
            if b == 0:
                continue
            else:
                return i, b
            pass
        pass

    @staticmethod
    def solve_eqn(equations):
        """
        Uisng Gauss-Jordan elimination
        1. each equation only consists of numbers or coefficients.
        2. variables are on the left and constants are on the right
        :param equations: Vector objects
        :return:
        """
        num_eqn = len(equations)  # number of equation
        zero_essentially = LinearAlg.find_lowest_order(equations)
        # print("zero = ", zero_essentially)
        assert zero_essentially >= 0
        for row in range(num_eqn):
            # print(">>>>>>>>>>>eqn ", row)
            col, pivot = LinearAlg.choose_pivot(equations[row])
            # print("pivot ", pivot)
            equations[row] /= pivot  # make the pivot 1
            # print("ROW eqn [", row, "] = ", equations[row])
            equations[row] = LinearAlg.apply_zero(equations[row].toList(), zero_essentially)
            # print(equations[row])
            for j in range(num_eqn):
                if row == j:
                    continue
                tmp = equations[j][col]
                # print("before eqn[", j, "] = ", equations[j])
                # print("operation => eqn[", j, "] = eqn[", j , "] - eqn[", row ,"] * (", tmp, ")")
                equations[j] = equations[j] - equations[row]*tmp
                # print("after eqn[", j, "] = ", equations[j])
                equations[j] = LinearAlg.apply_zero(equations[j].toList(), zero_essentially)
                # print("apply zero after eqn[", j, "] = ", equations[j])
                pass
            # print("all eqn")
            # for kk in range(num_eqn):
            #     print(equations[kk])
            pass

        solutions_a = []
        for row in range(num_eqn):
            solutions_a.append(equations[row][-1])

        return solutions_a

    @staticmethod
    def apply_zero(one_eqn, zero_essentially):
        for i in range(len(one_eqn)):
            if abs(one_eqn[i]) < zero_essentially:
                one_eqn[i] = 0
                pass
            pass
        return Vector(one_eqn)

    @staticmethod
    def find_lowest_order(equations):
        numbersss = [sys.float_info.max, 0]
        for eqn in equations:
            for elm in eqn.toList():
                if elm < numbersss[0]:
                    numbersss[0] = elm
                    pass
                if numbersss[1] < elm:
                    numbersss[1] = elm
                    pass
                pass
            pass
        # print(numbersss)
        return abs((numbersss[0] / numbersss[1])*1e-6)
        pass

    @staticmethod
    def solve(A_matrix, b_vector):
        """
        solve for x in
        A x = b
        using Gauss-Jordan Elimination
        :param A_matrix: a matrix
        :param b_vector: a vector
        :return: solution
        """

        pass


def test1():
    eq1 = Vector([7, 2, 3])
    eq2 = Vector([-5, 3, -2])
    print("before ")
    print(eq1)
    print(eq2)
    solutions = LinearAlg.solve_eqn([eq1, eq2])
    print(solutions)
    print("actual solution x= ", 0.419355, " y= ", 0.0322581)

def test2():

    eq1 = Vector([7,  2,  -3, 3])
    eq2 = Vector([-5, 3, 2, -2])
    eq3 = Vector([0, 3, -1, -2])
    print("before ")
    print(eq1)
    print(eq2)
    print(eq3)
    solutions = LinearAlg.solve_eqn([eq1, eq2, eq3])
    print(solutions)
    print("actual solution x= ", 1.39286, " y= ", 0.107143, " z= ",  2.32143)


def test3():
    eqn1 = Vector([41.8, 33, 10])
    eqn2 = Vector([33, 70.4, 11])
    print("before ")
    print(eqn1)
    print(eqn2)
    solns = LinearAlg.solve_eqn([eqn1, eqn2])
    print(solns)
    print("actual solutions x= ", 0.183954, " y= ", 0.0700214)

def test4():
    R2 = 5
    R3 = 10
    R10 = 7
    V1 = 2
    V2 = 3
    V3 = 5
    eqn3 = Vector([1, -1, -1, 0])
    eqn1 = Vector([-R2, 0, -R3, V3 - V1])
    eqn2 = Vector([0, -R10, R3, -V3 - V2])
    print("before ")
    print(eqn1)
    print(eqn2)
    print(eqn3)
    solns = LinearAlg.solve_eqn([eqn1, eqn2, eqn3])
    print(solns)
    print("actual solutions x= ", 0.187096774193548, " y= ", 0.580645161290323, " z= ", -0.393548387096774)

def test5():

    R1, R2, R3, R4, R5, R6, R7, E1, E2, E3 = 8, 8, 2, 2, 12, 2, 4, 10.0, 12.0, 12.0
    R1, R2, R3, R4, R5, R6, R7 = R1 * 1000, R2 * 1000, R3 * 1000, R4 * 1000, R5 * 1000, R6 * 1000, R7 * 1000

    R8 = 1 / (1 / R4 + 1 / R5)
    R9 = 1 / (1 / R6 + 1 / R7)
    R10 = R8 + R9


    eqn3 = Vector([1, -1, -1, 0])
    eqn1 = Vector([R2, 0, R3, -E3 + E1])
    eqn2 = Vector([0, R10, -R3, E3 + E2])


    print("before ")
    print(eqn1)
    print(eqn2)
    print(eqn3)
    solns = LinearAlg.solve_eqn([eqn1, eqn2, eqn3])
    print(solns)
    print("actual solutions x= ", 8.15573770491803e-7, " y= ", 5.07786885245902e-6, " z= ", -4.26229508196721e-6)
    assert abs(solns[0]) < 1
    assert abs(solns[1]) < 1
    assert abs(solns[2]) < 1

def test():
    test1()
    test2()
    test3()
    test4()
    test5()
