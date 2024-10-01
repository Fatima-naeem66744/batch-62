def manage_student_database():
    student_list: list[tuple] = []
    counter_id = 1

    while True:
        student_names = input("Write your name or enter 'stop' to execute:\t")

        if student_names == "":
            print("First, enter your name")
            continue

        if student_names.lower() == "stop":
            break

        if not student_names.isalpha():
            print("Please enter only alphabetic characters for the name.")
            continue

        if any(student_names == student[1] for student in student_list):
            print("Student already exists.")
        else:
            student_list.append((counter_id, student_names))
            counter_id += 1

    for student in student_list:
        print(student)

    print("\nFormatted List of Students:")
    for student in student_list:
        print(f"Student ID: {student[0]}, Name: {student[1]}")

    print(f"Total number of students:  {len(student_list)}")
    
    if student_list:
        total_name_length = sum(len(student[1]) for student in student_list)
        longest_name_student = max(student_list, key=lambda x: len(x[1]))
        shortest_name_student = min(student_list, key=lambda x: len(x[1]))

        print(f"Total length of all student names combined: {total_name_length}")
        print(f"Student with the longest name: {longest_name_student[1]}")
        print(f"Student with the shortest name: {shortest_name_student[1]}")
    else:
        print("\nNo students in the list.")

manage_student_database()
