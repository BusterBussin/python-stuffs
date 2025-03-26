def calcAverage(score1, score2, score3, score4, score5):
    average = float(score1 + score2 + score3 + score4 + score5)
    return average / 5
def determineGrade(score):
    if score > 9.1:
        return "Warning"
    if score > 6:
        return "Excel"
    if score > 3:
        return "Pass"
    if score <= 3 and score >= 1:
        return "Fail"
    return None
score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))
score3 = float(input("Enter the third score: "))
score4 = float(input("Enter the fourth score: "))
score5 = float(input("Enter the fifth score: "))
average = calcAverage(score1, score2, score3, score4, score5)
print("Here are the grades and the average.\nScore 1:", determineGrade(score1),"\nScore 2:", determineGrade(score2), "\nScore 3:", determineGrade(score3), "\nScore 4:", determineGrade(score4), "\nScore 5:", determineGrade(score5))
print("Average score:", average, "\nAverage Grade:", determineGrade(average))
