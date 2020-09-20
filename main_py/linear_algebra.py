from main_py import vector


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
        for row in range(num_eqn):
            # print(">>>>>>>>>>>eqn ", row)
            col, pivot = LinearAlg.choose_pivot(equations[row])
            equations[row] /= pivot  # make the pivot 1
            print(equations[row])
            for j in range(num_eqn):
                if row == j:
                    continue
                tmp = equations[j][col]
                # print("before ", equations[j])
                # print("operation => eqn[", j, "] = eqn[", j , "] - eqn[", row ,"] * (", tmp, ")")
                equations[j] = equations[j] - equations[row]*tmp
                # print("after ", equations[j])
                pass

        solutions_a = []
        for row in range(num_eqn):
            solutions_a.append(equations[row][-1])

        return solutions_a

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


def test():
    eq1 = vector.Vector([7,  2,  3])
    eq2 = vector.Vector([-5, 3, -2])
    print("before ")
    print(eq1)
    print(eq2)
    solutions = LinearAlg.solve_eqn([eq1, eq2])
    print(solutions)
    print("actual solution x= ", 0.419355, " y= ", 0.0322581)

    eq1 = vector.Vector([7,  2,  -3, 3])
    eq2 = vector.Vector([-5, 3, 2, -2])
    eq3 = vector.Vector([0, 3, -1, -2])
    print("before ")
    print(eq1)
    print(eq2)
    print(eq3)
    solutions = LinearAlg.solve_eqn([eq1, eq2, eq3])
    print(solutions)
    print("actual solution x= ", 1.39286, " y= ", 0.107143, " z= ",  2.32143)
    pass
