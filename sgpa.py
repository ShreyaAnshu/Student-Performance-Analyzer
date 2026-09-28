def calculate_sgpa(subjects):
    total_points = 0
    total_credits = 0

    for subject in subjects:
        total_points = total_points + (subject["credits"] * subject["grade_point"])
        total_credits = total_credits + subject["credits"]

    sgpa = total_points / total_credits

    return round(sgpa, 2)
