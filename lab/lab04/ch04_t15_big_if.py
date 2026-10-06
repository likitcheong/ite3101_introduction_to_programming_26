# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:  # 80 到 89
        return "B"
    elif grade >= 70:  # 70 到 79
        return "C"
    elif grade >= 65:  # 65 到 69
        return "D"
    else:              # 65 以下
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
