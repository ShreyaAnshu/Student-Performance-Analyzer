def calculate_cgpa(sgpas,credits_per_sem):
    total=0
    total_credits=0
    for i in range(len(sgpas)):
        total=total+sgpas[i]*credits_per_sem[i]
        total_credits += credits_per_sem[i]
        
    cgpa=total/total_credits
    return round(cgpa,2)
        
    
