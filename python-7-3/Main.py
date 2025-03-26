from ExamGrader import ExamGrader
def collect_answers(questions):
    userAnswers = []  # Start with an empty list

    for questionNumber in range(1, questions + 1):
        print(f"Question {questionNumber}:")
        answer = input().upper()  # Read input and convert to uppercase
        
        while answer not in ['A', 'B', 'C', 'D']:  # Validate input
            print("ERROR: Valid answers are A, B, C, or D. Please enter a valid answer.")
            answer = input().upper()
        
        userAnswers.append(answer)  # Store answer in the list
    
    return userAnswers
FINAL_QUESTIONS = 20
questionsMissed = []
answer = ""
print("Enter your answers to the exam questions. (Make sure Caps Lock is ON!)")
userAnswers = collect_answers(FINAL_QUESTIONS)
grade = ExamGrader(userAnswers)
grade.gradeExam()
questionsMissed = grade.questionsMissed()
numCorrect = grade.GETtotalCorrect()
numIncorrect = grade.GETtotalIncorrect()
print("Correct: " + str(numCorrect))
print("Incorrect:" + str(numIncorrect))
if grade.passed():
    print("You have passed the exam.")
else:
    print("You have failed the exam.")
if grade.GETtotalIncorrect() > 0:
    print ("You have missed the following questions: ")
    for i in range(len(questionsMissed)):
        if questionsMissed[i] > 0:
            print(questionsMissed[i])

        