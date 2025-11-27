# Initialize empty list to store students
# Each student will be represented as a dictionary with 'name' and 'grades' keys
students = []

def option1(students):
    """Add a new student to the system"""
    nameStudent = input("\nEnter student name: ")
    
    # Check if student already exists
    for student in students:
        if student['name'] == nameStudent:
            print("This student's name has already been added!")
            return
    
    # Add new student with empty grades list
    students.append({
        'name': nameStudent,
        'grades': []  # Initialize empty list for grades
    })
    print("Student's name successfully added!\n")

def option2(students):
    """Add grades for an existing student"""
    print("")
    nameStudent = input("Enter student's name: ")
    
    # Search for student in the list
    student_found = None
    for student in students:
        if student['name'] == nameStudent:
            student_found = student
            break
    
    if student_found:
        # Continue adding grades until user types 'done'
        while True:
            grade_input = input("Enter a grade (or 'done' to finish): ")
            
            # Exit condition - user types 'done'
            if grade_input.lower() == 'done':
                print(f"Finished adding grades for {nameStudent}\n")
                break
            
            try:
                # Convert input to integer
                gradeStudent = int(grade_input)
                
                # Validate grade range [0, 100]
                if 0 <= gradeStudent <= 100:
                    student['grades'].append(gradeStudent)  # Add grade to student's list
                    print("Grade added successfully!")
                else:
                    print("Grade must be between 0 and 100!!!")
                    
            except ValueError:
                # Handle non-numeric input
                print("Error: Please enter a valid number or 'done'!")
    else:
        print(f"Student's name {nameStudent} not found!!\n")

def option3(students):
    """Generate a comprehensive report of all students and their statistics"""
    print("\n---Student Report---")

    # Check if there are any students in the system
    if not students:
        print("No students in the system!")
        return
    
    # List to store averages for calculating overall statistics
    averages = []
    
    # Iterate through all students and calculate their averages
    for student in students:
        try:
            # Calculate average grade for student
            average = sum(student['grades']) / len(student['grades'])
            averages.append(average)  # Store for overall statistics
            print(f"{student['name']}'s average grade is {average:.2f}")
        except ZeroDivisionError:
            # Handle case where student has no grades
            print(f"{student['name']}'s average grade is N/A!")
    
    print("-----------------")

    # Calculate and display overall statistics if there are any grades
    if averages:
        # Find maximum, minimum and overall average
        maxAverage = max(averages)
        minAverage = min(averages)
        overallAverage = sum(averages) / len(averages)

        # Display statistics
        print(f"Max Average: {maxAverage:.2f}")
        print(f"Min Average: {minAverage:.2f}")
        print(f"Overall Average: {overallAverage:.2f}\n")
    else:
        # Added: Handle case where no students have grades
        print("No grades available in the system!")

def option4(students):
    """Find the student(s) with the highest average grade"""
    print("\n--- Top Performer ---")
    
    # Check if there are any students in the system
    if not students:
        print("No students in the system!")
        return
    
    # Filter students who have grades (exclude students with empty grade lists)
    students_with_grades = [student for student in students if student['grades']]
    
    # Check if any students have grades
    if not students_with_grades:
        print("No students have grades yet!")
        return
    
    # Use max() with a lambda function as the key to find highest average
    # Lambda function calculates average grade for each student
    top_student = max(students_with_grades, 
                     key=lambda student: sum(student['grades']) / len(student['grades']))
    
    # Calculate the highest average grade
    top_average = sum(top_student['grades']) / len(top_student['grades'])
    
    # Find all students with the same highest average (handle ties)
    top_students = []
    for student in students_with_grades:
        average = sum(student['grades']) / len(student['grades'])
        if average == top_average:
            top_students.append(student['name'])
    
    # Print the result - handle both single winner and ties
    if len(top_students) == 1:
        print(f"Top student: {top_students[0]} with average: {top_average:.2f}\n")
    else:
        print(f"Top students with average {top_average:.2f}: {', '.join(top_students)}\n")

# Main program loop
run = True
while run:
    # Display menu options
    print("---Student Grade Analyzer---")
    print("1. Add a new student")
    print("2. Add grades for student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")
    
    try:
        # Get user input for menu choice
        answer = int(input("Enter your choice: "))

        # Execute corresponding function based on user choice
        if answer == 1:
            option1(students)
        elif answer == 2:
            option2(students)
        elif answer == 3:
            option3(students)
        elif answer == 4:
            option4(students)
        elif answer == 5:
            print("Exiting...")
            run = False  # Fixed: Use run = False instead of exit()
        else:
            # Handle invalid menu choices
            print("Please enter number between 1 and 5!")
            
    except ValueError:  # Fixed: Catch specific ValueError instead of general Exception
        # Handle invalid input (non-numeric)
        print("Error: Please enter a valid number between 1 and 5!")