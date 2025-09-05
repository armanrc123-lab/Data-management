# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Arman Chowdhury"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324830"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "71"

#==========================================#
# Place your curve_fit function after this line

import numpy as np


def curve_fit(student_list: list[dict], comparison: str, degree: int) -> str:
    """This function takes a list of dictionaries containing the key G_Avg
    and returns a polynomial fit of a specified degree
    using interpolation between G_Avg and another specified key.
    Preconditions:
    student list contains G_Avg key with int/float value
    comparison key has int/float value

    >>>[
    {'School': 'MS', 'Age': 22, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7, 'G_Avg': 16},
    {'School': 'MS', 'Age': 24, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7, 'G_Avg': 17},
    {'School': 'MS', 'Age': 19, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7, 'G_Avg': 19}
])
    y = 0.3000000000000068x^2 + -13.300000000000521x^1 + 163.40000000000796
     """

    sum_dic = {}
    count_dic = {}

    for student in student_list:
        x = student[comparison]
        y = student['G_Avg']
        if x not in sum_dic:
            sum_dic[x] = y
            count_dic[x] = 1
        else:
            sum_dic[x] += y
            count_dic[x] += 1

    x, y = [], []

    for key in sum_dic:
        x.append(key)
        y.append(sum_dic[key] / count_dic[key])

    result = "y = "

    if degree >= len(x):
        degree = len(x) - 1

    array = np.polyfit(x, y, degree)

    for i in range(len(array)):
        if i != len(array) - 1:
            result += str(array[i]) + "x^" + str(degree - i) + " + "
        else:
            result += str(array[i])

    return result


# Do NOT include a main script in your submission
