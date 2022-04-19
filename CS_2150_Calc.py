# CS 2150 Spring 2022 UVA
# 45% Labs
# 30% Midterm Exams (2)
# 25% Final

lab_avg = float(input("Please enter your lab average: "))
midterm_avg = float(input("Please enter your midterm average: "))
final_avg = float(input("Please enter you final exam grade: "))

def final_grade(lab, midterm, final) : 
    return((lab*.45)+(midterm*.30)+(final*.25))

print(final_grade(lab_avg, midterm_avg, final_avg))