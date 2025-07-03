student_grades = {}

while True:
    print("\n1. Add/Update Student")
    print("2. Print All Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_grades[name] = grade
        print(f"{name}'s grade has been added/updated.")
    
    elif choice == '2':
        print("\n--- Student Grades ---")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
