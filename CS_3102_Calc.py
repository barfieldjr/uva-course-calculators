# CS 3102 Spring 2022 UVA
# 50% Quizzes
# 50% Problem Sets

quiz_avg = int(input("Please enter your quiz average: "))
pset_avg = int(input("Please enter your problem set average: "))

def final_grade(quiz, pset) : 
    return((quiz*.5)+(pset*.50))

print(final_grade(quiz_avg, pset_avg))