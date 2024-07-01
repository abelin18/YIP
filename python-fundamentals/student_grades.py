student_grades = [("Billy", 93), ("Jen", 82), ("Max", 98), ("Anne", 65), ("Charlie", 71)]

for record in student_grades:
    name, grade = record
    print("The grade is {1} from {0}" .format(name, grade))
   