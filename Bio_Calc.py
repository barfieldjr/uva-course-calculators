# Biology Spring 2022 UVA
# 70% Exams
# 20% Lab
# 10% Mastering Biology

exam_avg = 0
lab_avg = 0
mast_avg =  0

def final_grade(exam, lab, mast) :
    return (exam*.7)+(lab*.2)+(mast*.1)

print(final_grade(exam_avg, lab_avg, mast_avg))