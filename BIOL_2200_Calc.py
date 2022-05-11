# BIOL 2200 Spring 2022 UVA
# 70% Exams
# 20% Lab
# 10% Mastering Biology

exam_avg = float(input("Please enter your exam average: "))
lab_avg = float(input("Please enter your lab average: "))
mast_avg =  float(input("Please enter your Mastering Biology average: "))
poll = float(input("What percentage of the poll everywhere questions have you answered? \n(Ex: If you have completed around half of the questions enter 50, if you have completed all of them please enter 100): "))
exam_wrapper = str(input("Did you complete the exam wrapper? Enter 'True' or 'False': "))

def final_grade(exam, lab, mast, poll, wrap) :
    if wrap == 'True':
        return (exam*.7)+(lab*.2)+(mast*.1)+(poll*.01)+.35
    return (exam*.7)+(lab*.2)+(mast*.1)+(poll*.01)

print("Your final grade calculation: " + str(final_grade(exam_avg, lab_avg, mast_avg, poll, exam_wrapper)))