from main_py import vector

class Matrix:
    """
    matrix class
    """

    def __init__(self, matrix):
        """
        Each row of matrix is a plain list
        """
        self.matrix = matrix
        self.row_count = self.row(matrix)
        self.col_count = self.col(matrix)

    def get_list(self):
        return self.matrix

    @staticmethod
    def row(matrix):
        # print(matrix)
        return len(matrix)

    @staticmethod
    def col(matrix):
        row_count = Matrix.row(matrix)
        col_count = len(matrix[0])
        print(row_count)
        print(col_count)
        return col_count

    def print_mat(self):
        print("[", end="")
        for i in range(self.row_count):

            if i < self.row_count-1:
                print(self.matrix[i], ",")
            else:
                print(self.matrix[i], "]")
        pass

    # def __get_matrix(self, matrix):
    #     if type(matrix) == Matrix:
    #         # print("matrix.matrix")
    #         # print(matrix.matrix)
    #         return matrix.matrix
    #     else:
    #         return matrix
    #     pass

    @staticmethod
    def matmul(matA, matB):
        """
        Matrix multiplication.
        C = A B
        C[i,j] = A[i,k] B[k, j]
        """

        rAA = Matrix.row(matA)
        cAA = Matrix.col(matA)

        rBB = Matrix.row(matB)
        cBB = Matrix.col(matB)


        matOut = []
        if cAA != rBB:
            print("col(A) != row(B)")
            return None
        for i in range(rAA):
            one_row = []
            for j in range(cBB):
                tmp = 0
                for k in range(cAA):
                    tmp += matA[i][k] * matB[k][j]
                    pass
                print(matOut)
                one_row.append(tmp)
                pass
            matOut.append(one_row)
            pass
        return Matrix(matOut)

    def determinant(self):

        pass

    def apply(self, func):
        """
        apply a function to all elements of a matrix
        :param func:
        :return:
        """

        pass

    pass



if __name__ == '__main__':
    a = [1,2]
    b = [4,2]
    matA = Matrix([a,b])
    matA.print_mat()

    # matC = matA.matmul(matA)
    # print(matC)

    matA = [[1, 2, 3], [4, 5, -6], [6, 6, 6]]
    matB = [[1, 2, 3], [4, 5, -6], [1, -6, -6]]

    matC = Matrix.matmul(matA, matB)
    matC.print_mat()
    print(matC)

