"""
Project 06: The Automatic Grader (Nested Lists)
Scenario: You have a list of correct answers for a test. You also have a list of students, where each student is represented by a list containing their name and their answers. You need to grade them.

Functional Requirements:

Master Answer Key: ['A', 'B', 'A', 'C', 'D']
Student Data (Nested List): [["John", ['A', 'B', 'B', 'C', 'D']], ["Jane", ['A', 'A', 'A', 'A', 'A']]]
Loop through every student.
Inside that loop, loop through their answers.
Compare student_answer[i] vs key[i]. Calculate a score.
Print a report card: "John: 4/5 (80%)".
"""

answers=input("Enter answer key:").split(",")
total_students=int(input("Enter total no of students:"))

student_details={}

for i in range(total_students):
    student_name=input(f"Enter Student{i+1} name:")
    student_answer=input(f"Enter Student{i+1} answers:").split(",")
    student_details[student_name]=student_answer
    



def calc_marks(ls):
    total_marks=0
    for i in range(len(ls)):
        if ls[i]==answers[i]:
            total_marks+=1

    return total_marks

score_card=[]

for key,value in student_details.items():
    student_score_card={}
    student_score_card["Name"]=key
    student_score_card["Correct Answer"]=calc_marks(value)
    student_score_card["Percentage"]=(calc_marks(value)*100)/len(value)
    score_card.append(student_score_card)

print(f"All students Score Cards:{score_card}")









