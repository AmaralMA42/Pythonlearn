class Matrix:
    def __init__(self):
        self.size = self.get_dimensions()
        self.bulk = self.get_matrix(self.size)

    def get_dimensions(self):
        size = list(input("Enter size of matrix:").replace(" ", ""))
        return [int(i) for i in size]

    def get_matrix(self, size_vec):
        matrix = []
        print("Enter matrix")
        for i in range(size_vec[0]):
            line = input().split(" ")
            matrix.append([float(j) for j in line])
        return matrix

    def call_add(self, b):
        size1 = self.size
        matrix1 = self.bulk
        # print(matrix1)
        size2 = b.size
        matrix2 = b.bulk
        # print(matrix2)
        if size1 != size2:
            print("The operation cannot be performed.")
        else:
            for i in range(size2[0]):
                for j in range(size2[1]):
                    matrix2[i][j] += matrix1[i][j]
            print_matrix(size2[0], size2[1], matrix2)

    def call_mult_const(self, scalar):
        size = self.size
        matrix1 = self.bulk
        # print(matrix1)
        for i in range(size[0]):
            for j in range(size[1]):
                matrix1[i][j] *= scalar
        return matrix1

    def call_mult_matr(self, second_matrix):
        size1 = self.size
        matrix1 = self.bulk
        # print(matrix1)
        size2 = second_matrix.size
        matrix2 = second_matrix.bulk
        # print(matrix2)
        if size1[1] != size2[0]:
            print("The operation cannot be performed.")
        else:
            matrix3 = []
            for i in range(size1[0]):  # row
                line = []
                for j in range(size2[1]):  # column
                    aux = 0
                    for k in range(size2[0]):  # column
                        aux += matrix1[i][k] * matrix2[k][j]
                    line.append(aux)
                matrix3.append(line)
            print_matrix(size1[0], size2[1], matrix3)

    def call_main_tran(self):
        size = self.size
        matrix = self.bulk
        matrix3 = []
        for i in range(size[0]):  # row
            line = []
            for j in range(size[1]):  # column
                line.append(matrix[j][i])
            matrix3.append(line)
        print_matrix(size[0], size[1], matrix3)

    def call_sid_tran(self):
        size = self.size
        matrix = self.bulk
        matrix3 = []
        for i in range(size[0]):  # row
            line = []
            for j in range(size[1]):  # column
                line.append(matrix[-j - 1][-i - 1])  # row,column
            matrix3.append(line)
        print_matrix(size[0], size[1], matrix3)

    def call_ver_tran(self):
        size = self.size
        matrix = self.bulk
        matrix3 = []
        for i in range(size[0]):  # row
            line = []
            for j in range(size[1]):  # column
                line.append(matrix[i][-j - 1])  # row,column
            matrix3.append(line)
        print_matrix(size[0], size[1], matrix3)

    def call_hor_tran(self):
        size = self.size
        matrix = self.bulk
        matrix3 = []
        for i in range(size[0]):  # row
            line = []
            for j in range(size[1]):  # column
                line.append(matrix[-i - 1][j])  # row,column
            matrix3.append(line)
        print_matrix(size[0], size[1], matrix3)

    def recurentdet(self, matrix_, size):
        if size == [1, 1]:
            return matrix_[0][0]
        elif size == [2, 2]:
            return matrix_[0][0] * matrix_[1][1] - matrix_[0][1] * matrix_[1][0]
        else:
            det = 0
            subsize = [size[0] - 1, size[1] - 1]
            for i in range(size[1]):
                submatrix = [[matrix_[k][j] for j in range(size[1]) if j != i] for k in range(1, size[0])]
                det += matrix_[0][i] * self.recurentdet(submatrix, subsize) * (-1) ** (1 + i + 1)
            return det

    def call_inverse(self):
        determinant = self.recurentdet(a.bulk, a.size)
        if determinant == 0:
            return print("error")
        size = self.size
        maux = [[self.bulk[l][k] for k in range(size[1])] for l in range(size[0]) ]
        subsize = [size[0] - 1, size[1] - 1]
        for i in range(size[0]):  # row
            for j in range(size[1]):  # colum
                term = (-1) ** (i + j + 2)
                sub_matrix = [[self.bulk[l][k] for k in range(size[1]) if k != i]
                              for l in range(size[0]) if l != j]
                maux[i][j] = term * self.recurentdet(sub_matrix, subsize) / determinant
        print_matrix(size[0], size[1], maux)


def print_matrix(y, x, matrix):
    print("The result is: ")
    for i in range(y):
        for j in range(x):
            if j == x - 1:
                print(str(round(matrix[i][j],2)) + " ")
            else:
                print(str(round(matrix[i][j],2)) + " ", end='')


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Calculate inverse
0. Exit""")
    choice = input("Your choice: >")
    if choice == "1":
        a = Matrix()
        b = Matrix()
        a.call_add(b)
    elif choice == "2":
        a = Matrix()
        scalar = int(input("Enter constant: "))
        new_a = a.call_mult_const(scalar)
        print_matrix(a.size[0], a.size[1], new_a)
    elif choice == "3":
        a = Matrix()
        b = Matrix()
        a.call_mult_matr(b)
    elif choice == "4":
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        choice2 = input("Your choice: >")
        if choice2 == "1":
            a = Matrix()
            a.call_main_tran()
        elif choice2 == "2":
            a = Matrix()
            a.call_sid_tran()
        elif choice2 == "3":
            a = Matrix()
            a.call_ver_tran()
        elif choice2 == "4":
            a = Matrix()
            a.call_hor_tran()
    elif choice == "5":
        a = Matrix()
        if a.size[0] != a.size[1]:
            print("The operation cannot be performed.")
        else:
            determinant = a.recurentdet(a.bulk, a.size)
            print("The determinant 2 is: ")
            print(determinant)
    elif choice == "6":
        a = Matrix()
        if a.size[0] != a.size[1]:
            print("The operation cannot be performed.")
        else:
            a.call_inverse()
    elif choice == "0":
        print("Program end")
        break
    else:
        print("No valid option")
