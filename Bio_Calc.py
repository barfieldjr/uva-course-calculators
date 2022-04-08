# Biology Spring 2022 UVA
# 70% Exams
# 20% Lab
# 10% Mastering Biology

exam_avg = int(input("Please enter your exam average: "))
lab_avg = int(input("Please enter your lab average: "))
mast_avg =  int(input("Please enter your Mastering Biology average: "))

def final_grade(exam, lab, mast) :
    return (exam*.7)+(lab*.2)+(mast*.1)

print(final_grade(exam_avg, lab_avg, mast_avg))