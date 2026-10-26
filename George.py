user = "Martin"
print("Hello, I am", user)
user = "George"
print("Hello, I am" , user)
print(type(user))
name = "martin"
age = 53
height = 1.75
student_now = True
print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))
city = "Poznan"
print(city)
print(type(city))
slices_per_student = 3
students = 14
present_students = students - 4
total_slices_needed = slices_per_student * present_students
cost_per_student = 500 / present_students
boxes_to_order = (total_slices_needed // 8) + 1  
leftover_slices = (boxes_to_order * 8) % present_students
