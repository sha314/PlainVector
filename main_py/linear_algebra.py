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
        for row in range(num_eqn):
            # print(">>>>>>>>>>>eqn ", row)
            col, pivot = LinearAlg.choose_pivot(equations[row])
            equations[row] /= pivot  # make the pivot 1
            # print(equations[row])
            equations[row] = LinearAlg.apply_zero(equations[row].toList(), zero_essentially)
            # print(equations[row])
            for j in range(num_eqn):
                if row == j:
                    continue
                tmp = equations[j][col]
                # print("before ", equations[j])
                # print("operation => eqn[", j, "] = eqn[", j , "] - eqn[", row ,"] * (", tmp, ")")
                equations[j] = equations[j] - equations[row]*tmp
                equations[j] = LinearAlg.apply_zero(equations[j].toList(), zero_essentially)
                # print("after ", equations[j])
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
        return (numbersss[0] / numbersss[1])*1e-6
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

def test():
    test1()
    test2()
    test3()
