attendance = {}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    students = input("Enter students present on " + day + " (separated by spaces): ")
    attendance[day] = set(students.split())

all_students = attendance[days[0]]
for day in days[1:]:
    all_students = all_students.intersection(attendance[day])

student_count = {}

for day in days:
    for student in attendance[day]:
        if student in student_count:
            student_count[student] += 1
        else:
            student_count[student] = 1

one_day_students = set()

for student, count in student_count.items():
    if count == 1:
        one_day_students.add(student)

unique_students = set()

for day in days:
    unique_students = unique_students.union(attendance[day])

print("\nAttendance Record:")
for day in days:
    print(day, ":", attendance[day])

print("\nStudents who attended all classes:")
print(all_students)

print("\nStudents who attended only one class:")
print(one_day_students)

print("\nTotal unique students:", len(unique_students))
print(unique_students)