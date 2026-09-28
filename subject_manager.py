def get_subjects():
    subjects=[]
    numbers_of_subjects=int(input("enter the numbers of subjects:"))
    
    for i in range(numbers_of_subjects):
        print(f"\n------subject{i+1}-------")
        
        name=input("enter the subject name : ")
        credits=float(input("enter the credits of the subjects :"))
        grade_point = float(input("enter the grade obtained by the student: "))
        #making new dictionary!!
        subject={ "name":name , "credits":credits , "grade_point":grade_point }
        #adding that dictionary to the list we made initially 
        subjects.append(subject)
    return subjects