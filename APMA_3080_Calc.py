# APMA 3080 Spring 2022 UVA
# 30% Final Exam
# 30% Midterm Exams (2)
# 20% Labs and Projects 
# 10% In-class activites
# 5% Webwork
# 5% Other (Not defined so just added in calculation)

final_avg = float(input("Please enter your final exam grade: "))
midterm_avg = float(input("Please enter your midterm average: "))
labs_avg = float(input("Please enter you labs and projects average: "))
in_class = float(input("Please enter your in-class activites average: "))
webwork = float(input("Please enter your webwork average: "))


def final_grade(final, midterm, labs, ica, webwork) : 
    return((final*.30)+(midterm*.30)+(labs*.20)+(ica*.1)+(webwork*.05)+.05)

print(final_grade(final_avg, midterm_avg, labs_avg, in_class, webwork))