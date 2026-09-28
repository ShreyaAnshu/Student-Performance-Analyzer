from student_profile import student_profile_data
from subject_manager import get_subjects
from sgpa import calculate_sgpa
from cgpa import calculate_cgpa
from performance import performance_analysis
print("==========================================================")
print("              COLLEGE PERFORMANCE ANALYZER                ")
print("==========================================================")
print("welcome!")
print("This programme analyses the performance of every student.")

name,reg,branch,year= student_profile_data()


print("=============================================================")
print("______________________STUDENT PROFILE________________________")

print("NAME:",name)
print("REGISTRATION NO:",reg)
print("BRANCH:",branch)
print("YEAR:",year)


print("===============================================================")

print("====================SGPA CALCULATION FOR EACH SEMESTER=========================")


sgpas = []
credits_per_sem = []

number_of_semesters = int(input("Enter the number of semesters: "))

for semester in range(1, number_of_semesters + 1):
    print(f"\n---------- SEMESTER {semester} ----------")
    subjects = get_subjects()
    sgpa = round(calculate_sgpa(subjects),2)
    sgpas.append(sgpa)
    total_credits = 0
    for subject in subjects:
        total_credits=total_credits + subject["credits"]
        credits_per_sem.append(total_credits)
        
        
        
    
    
    print("====================SGPA CALCULATION===============================")
    print( "SGPA of Semester",semester,":",sgpa)
    
    
    print("THE LIST OF SGPAS IS GIVEN:")
    
    
    print("the sgpas of all the semester is:",sgpas)
    
    print("THE LIST OF CREDITS EARNED IS:")
    
    print("the credits earned:",credits_per_sem)
    
    

print("SGPA CALCULATION DONE!!!!")




print("==================CGPA CALCULATION==================")
CGPA=calculate_cgpa(sgpas,credits_per_sem)



print("YOUR CGPA IS :",CGPA)



print("CGPA CALCULATION DONE!!!!!")


print("=================================================================")
print("=====================PERFORMANCE=================================")

result,feedback=performance_analysis(CGPA)



print(result)
print(feedback)
