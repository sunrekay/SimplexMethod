class Simplex:
    def __init__(self, _matrix, row_size_t, column_size_t, x_list):
        self.row_size = row_size_t
        self.column_size = column_size_t
        self.main_matrix = self.fill_matrix(x_list, _matrix, row_size_t, column_size_t)
        self.start_simplex_method()

    def fill_matrix(self, x_list, _matrix, row_size_t, column_size_t):
        z = 0
        main_matrix = []
        for i in range(row_size_t):
            temp = []
            for j in range(column_size_t):
                temp.append(_matrix[z])
                z += 1
            main_matrix.append(temp)

        x_list.insert(0, 0)
        for i in range(len(x_list)):
            x_list[i] = 0 - x_list[i]
        main_matrix.append(x_list)

        for i in range(row_size_t):
            temp = [0 for i in range(row_size_t)]
            temp[i] = 1
            main_matrix[i] += temp
        temp = [0 for i in range(row_size_t)]
        main_matrix[len(main_matrix)-1] += temp
        return main_matrix

    def create_copy(self, matrix):
        new_matrix = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(0)
            new_matrix.append(temp)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[i][j] = matrix[i][j]
        return new_matrix

    def start_simplex_method(self):

        for i in self.main_matrix:
            print(i)
        print()

        r_list = []
        while min(self.main_matrix[len(self.main_matrix)-1]) < 0:
            temp = [0]
            for i in self.main_matrix[len(self.main_matrix)-1][1:]:
                if i < 0:
                    temp.append(abs(i))
                else:
                    temp.append(0)
            r_column = temp.index(max(temp))

            temp = []
            for i in range(self.row_size):
                if self.main_matrix[i][r_column] > 0:
                    temp.append(self.main_matrix[i][0]/self.main_matrix[i][r_column])
            r_row = temp.index(min(temp))

            r_list.append([r_row, r_column])
            r_element = self.main_matrix[r_row][r_column]

            new_matrix = self.create_copy(self.main_matrix)

            for j in range(len(new_matrix[r_row])):
                if r_element != 0:
                    new_matrix[r_row][j] = new_matrix[r_row][j] / r_element

            for i in range(len(new_matrix)):
                if i != r_row:
                    new_matrix[i][r_column] = 0

            for i in range(len(self.main_matrix)):
                for j in range(len(self.main_matrix[i])):
                    if (i == r_row) or (j == r_column):
                        pass
                    else:
                        if r_element != 0:
                            new_matrix[i][j] = new_matrix[i][j] - (self.main_matrix[i][r_column] * self.main_matrix[r_row][j])/r_element

            self.main_matrix = self.create_copy(new_matrix)
            for i in new_matrix:
                print(i)
            print()
        for i in r_list:
            print("x{}. {}".format(i[1], round(self.main_matrix[i[0]][0], 2)))
        print('F(X) = ' + str(round(self.main_matrix[len(self.main_matrix)-1][0],2)))


if __name__ == "__main__": # Пример ввода данных
    x_list = [15, 5, 3, 20]
    row_size = 2
    column_size = 5
    start_matrix = [1200, 4, 2, 1, 4,
                    1000, 1, 5, 3, 1]
    A = Simplex(start_matrix, row_size, column_size, x_list)
