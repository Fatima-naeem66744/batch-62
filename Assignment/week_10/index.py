"""1. Create the Student Class"""
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        total_score = sum(self.scores)
        num_subjects = len(self.scores)
        average_score = total_score / num_subjects
        return average_score

    def is_passing(self):
        average_score = self.calculate_average()
        passing_score = 60
        return average_score >= passing_score

"""2. Create the PerformanceTracker Class"""

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        new_student = Student(name, scores)
        self.students[name] = new_student

    def calculate_class_average(self):
        total_score = 0
        num_students = len(self.students)
        for student in self.students.values():
            total_score += student.calculate_average()
        class_average = total_score / num_students
        return class_average

    def display_student_performance(self):
        for student_name, student in self.students.items():
            average_score = student.calculate_average()
            passing_status = student.is_passing()
            print(f"{student_name}'s average score: {average_score}")
            print(f"{student_name}'s passing status: {passing_status}")
            print()

tracker = PerformanceTracker()

"""3. Handle User Input"""
while True:
    try:
        name = input("Enter student's name (or 'exit' to stop): ")
        if name.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            scores = []
            for i in range(3):
                score = float(input(f"Enter score for subject {i+1}: "))
                scores.append(score)

            tracker.add_student(name, scores)

            """4. Calculate Averages and Display Performance"""
            tracker.display_student_performance()
            class_average = tracker.calculate_class_average()
            print(f"Class average score: {class_average}\n")

    except ValueError:
        print("Please enter a valid number for the scores, not letters.")
