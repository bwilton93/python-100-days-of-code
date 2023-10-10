# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

array_length = 0
total_height = 0

for student_height in student_heights:
    array_length += 1
    total_height += student_height

print(f"total height = {total_height}")
print(f"number of students = {array_length}")
print(f"average height = {round(total_height / array_length)}")
