# Create an empty list to store student information
students = []

# Function to add a student
def add_student(name, grade):
    student = {"name": name, "grade": grade}
    students.append(student)
    print(f"Student {name} with grade {grade} added successfully.")

# Function to remove a student
def remove_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"Student {name} removed successfully.")
            return
    print(f"Student {name} not found.")

# Function to get all students
def get_all_students():
    return students

# Function to calculate the average grade
def get_average_grade():
    total = sum(student["grade"] for student in students)
    average = total / len(students)
    return average

# Add students
add_student("John", 85)
add_student("Alice", 92)
add_student("Bob", 78)

# Get all students
all_students = get_all_students()
for student in all_students:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

# Remove a student
name_to_remove = input("Enter the name of the student to remove: ")
remove_student(name_to_remove)

# Get average grade
average_grade = get_average_grade()
print(f"Average Grade: {average_grade}")
