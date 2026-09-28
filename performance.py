def performance_analysis(CGPA):
    if CGPA>=9:
        result="S grade!!"
        feedback="exellent performance"
    elif CGPA>=8:
        result="A grade!!"
        feedback="very good performance"
    elif CGPA>=7:
        result="B grade!!"
        feedback="average"
    elif CGPA>=6:
        result="C grade!!"
        feedback="need to work hard"
    elif CGPA>=5:
        result="D grade!!"
        feedback="bad performance"
    else:
        result="N grade"
        feedback=" very poor performance"
    return result,feedback
