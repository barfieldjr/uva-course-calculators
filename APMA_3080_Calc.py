# APMA 3080 Spring 2022 UVA
# 30% Final Exam
# 30% Midterm Exams (2)
# 20% Labs and Projects 
# 10% In-class activites
# 5% Webwork
# 5% Other

final_avg = int(input("Please enter your final exam grade: "))
midterm_avg = int(input("Please enter your midterm average: "))
labs_avg = int(input("Please enter you labs and projects average: "))
in_class = int(input("Please enter your in-class activites average: "))
webwork = int(input("Please enter your webwork average: "))


def final_grade(lab, midterm, final) : 
    return((lab*.45)+(midterm*.30)+(final*.25))

print(final_grade(lab_avg, midterm_avg, final_avg))