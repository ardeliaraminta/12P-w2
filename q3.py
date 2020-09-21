total_class1 = int(input("Input number of students for first class: "))
division_class1 = int(input(" Input number of groups for first class:"))

total_class2 = int(input("Input number of students for second class: "))
division_class2 = int(input(" Input number of groups for second class:"))

total_class3 = int(input("Input number of students for second class: "))
division_class3 = int(input(" Input number of groups for second class:"))

students_per_group1, leftover1 = divmod (total_class1, divisions_class1)
students_per_group2, leftover2 = divmod (total_class2, divisions_class2)
students_per_group3, leftover3 = divmod (total_class3, divisions_class3)

print("Number of students in each group:")
print("Class 1:", students_per_group1)
print("Class 1:", students_per_group2)
print("Class 1:", students_per_group3)
print("")
print("Number of students leftover:")
print("Class 1:", leftover1)
print("Class 2:", leftover2)
print("Class 3:", leftover3)