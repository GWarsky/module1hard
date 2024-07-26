grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
srednee1 = sum(grades[0]) / len(grades[0])
srednee2 = sum(grades[1]) / len(grades[1])
srednee3 = sum(grades[2]) / len(grades[2])
srednee4 = sum(grades[3]) / len(grades[3])
srednee5 = sum(grades[4]) / len(grades[4])
my_dict = [[students[0], srednee1], [students[1], srednee2], [students[2],
          srednee3], [students[3], srednee4], [students[4], srednee5]]
my_dict = dict(my_dict)
print(my_dict)
