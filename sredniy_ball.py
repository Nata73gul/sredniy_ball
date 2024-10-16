grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_list = list(grades)
students_list = list(students)
students_list.sort()
sredniy_ball = ((students_list[0]), sum(grades_list[0]) / len(grades_list[0]),
                (students_list[1]), sum(grades_list[1]) / len(grades_list[1]),
                (students_list[2]), sum(grades_list[2]) / len(grades_list[2]),
                (students_list[3]), sum(grades_list[3]) / len(grades_list[3]),
                (students_list[4]), sum(grades_list[4]) / len(grades_list[4]))

print(sredniy_ball)
