# ECE 2330 Spring 2022 UVA
# 30% Tests (3)
# 25% Project
# 20% Zybook challenge activities
# 15% Final exam
# 10% Zybook participation activities

test_avg = int(input("Please enter your test average: "))
proj_avg = int(input("Please enter your project average: "))
chal_avg = int(input("Please enter your Zybook challenge activities average: "))
part_avg = int(input("Please enter your Zybook participation activities average: "))
finl_avg = int(input("Please enter your final exam grade: "))

def final_grade(test, proj, chal, part, finl) : 
    return((test*.3)+(proj*.25)+(chal*.2)+(part*.1)+(finl*.15))

print(final_grade(test_avg, proj_avg, chal_avg, part_avg, finl_avg))