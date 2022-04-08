# CS 2150 Spring 2022 UVA
# 45% Labs
# 30% Midterm Exams (2)
# 25% Final

lab_avg = 0
midterm_avg = 0
final_avg = 0

def final_grade(lab, midterm, final) : 
    return((lab*.45)+(midterm*.30)+(final*.25))

print(final_grade(lab_avg, midterm_avg, final_avg))