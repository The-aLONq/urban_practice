grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #оценки в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
#print(students_sorted)

one = sum(grades[0])
one_1 = len(grades[0])
one_2 = one/one_1

two = sum(grades[1])
two_1 = len(grades[1])
two_2 = two/two_1

three = sum(grades[2])
three_1 = len(grades[2])
three_2 = three/three_1

four = sum(grades[3])
four_1 = len(grades[3])
four_2 = four/four_1

five = sum(grades[4])
five_1 = len(grades[4])
five_2 = five/five_1

dictionary = dict(zip(students_sorted, [one_2, two_2, three_2, four_2, five_2]))
print(dictionary)
