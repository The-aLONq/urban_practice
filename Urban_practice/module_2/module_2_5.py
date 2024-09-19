def get_matrix (n, m, value):
    if n < 1 or m < 1 or value < 1:
        print("Введите значение больше 0!")
        return
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    print(matrix)

get_matrix(3,5,-7)
