# Function to analyze performance based on marks
def analyze_performance(marks):

    total_marks = sum(marks)
    num_subjects = len(marks)
    average_marks = total_marks / num_subjects if num_subjects > 0 else 0

    # Determine performance category
    if average_marks >= 90:
        performance = "Excellent"
        tips = ["Keep up the great work!", "Consider helping others who are struggling."]
    elif average_marks >= 75:
        performance = "Good"
        tips = ["Maintain your study habits.", "Try to challenge yourself with advanced topics."]
    elif average_marks >= 50:
        performance = "Average"
        tips = ["Identify subjects you struggle with and focus on them.", "Consider forming a study group."]
    else:
        performance = "Needs Improvement"
        tips = ["Review your study techniques.", "Seek help from teachers or tutors."]

    return average_marks, performance, tips

# Function to analyze subject-wise performance
def analyze_subjects(subjects, marks):

    subject_analysis = {}
    
    for subject, mark in zip(subjects, marks):
        if mark >= 90:
            subject_analysis[subject] = "Excellent - Keep it up!"
        elif mark >= 75:
            subject_analysis[subject] = "Good - Maintain your study habits."
        elif mark >= 50:
            subject_analysis[subject] = "Average - Focus on improvement."
        else:
            subject_analysis[subject] = "Needs Improvement - Seek help and review techniques."

    return subject_analysis

# Main function to get user input and display results
def main():
    
        # Get subjects and marks from user
        subjects_input = input("Enter your subjects separated by commas: ")
        marks_input = input("Enter your marks for each subject separated by spaces: ")

        # Convert input to lists
        subjects = [subject.strip() for subject in subjects_input.split(',')]
        marks = list(map(int, marks_input.split()))

        # Analyze overall performance
        average_marks, performance, tips = analyze_performance(marks)

        # Analyze subject-wise performance
        subject_analysis = analyze_subjects(subjects, marks)

        # Display overall results
        print(f"\nYour Average Marks: {average_marks:.2f}")
        print(f"Performance Category: {performance}")
        print("Tips for Improvement:")
        for tip in tips:
            print(f"- {tip}")

        # Display subject-wise results
        print("\nSubject-wise Performance Analysis:")
        for subject, feedback in subject_analysis.items():
            print(f"{subject}: {feedback}")

# Run the main function
if __name__ == "__main__":
    main()