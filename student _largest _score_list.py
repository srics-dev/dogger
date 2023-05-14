students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Sort the students list by grade
students.sort(key=lambda x: x[1])

# Find the second lowest grade
second_lowest = None
for student in students:
    print(student)
    if second_lowest is None:
        second_lowest = student[1]
    elif student[1] > second_lowest:
        break
    elif student[1] < second_lowest:
        second_lowest = student[1]

# Print the names of students with the second lowest grade
for student in students:
    if student[1] == second_lowest:
        print(student[0])
