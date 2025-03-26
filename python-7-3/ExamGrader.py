class ExamGrader:
    def __init__(self, userAnswers):
        self.userAnswers = userAnswers
        self.correctAnswers = ['B', 'C', 'A', 'A', 'C', 'B', 'B', 'A', 'C', 'D', 
                               'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
        
        self.totalCorrect = 0
        self.totalIncorrect = 0
        self.missedQuestions = []
    def addMissedAnswer(self, index):
        self.missedQuestions.append(index)
    def gradeExam(self):
        for i in range(len(self.correctAnswers)):
            if self.userAnswers[i] == self.correctAnswers[i]:
                self.totalCorrect = self.totalCorrect + 1
            else:
                self.totalIncorrect = self.totalIncorrect + 1
                self.addMissedAnswer(i)
    def ExamGrader(self, userAnswers):
        self.userAnswers = userAnswers
        self.gradeExam
    def passed(self):
        if self.totalCorrect >= 15:
            return True
        else:
            return False
    def GETtotalCorrect(self):
        return self.totalCorrect
    def GETtotalIncorrect(self):
        return self.totalIncorrect
    def questionsMissed(self):
        return self.missedQuestions