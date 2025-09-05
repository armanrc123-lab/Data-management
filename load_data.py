# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
import string
__author__ = "Liam Cooper, Arman Chowdhury, Lucas Hiscocks, Benjamin Robert"

# Update "" with your team (e.g. T102)
__team__ = "T71"

#==========================================#
# Place your student_school_list function after this line


def student_school_list(filename: str, schoolname: str) -> list:
    """
    Return list of students from filename that attended schoolname
    Precondition: returned list will contain dictionaries for each student,
    containing all linked attributes except school
    >>>student_school_list('student-mat.csv', 'CF')
    [{'Age': 16, 'StudyTime': 4, 'Failures': 0, 'Health': 1, 'Absences': 0,
    'G1': 19, 'G2': 18, 'G2': 17}, {'Age': 18, 'StudyTime': 2, 'Failures': 0,
    'Health': 3, 'Absences': 10, 'G1': 13, 'G2': 10, 'G3': 11}]
    >>>student_school_list('student-mat.csv', 'Glebe')
    []
    """
    final_list = []
    header = []
    infile = open(filename, "r")
    for line in infile:
        line = line.strip()
        line = line.split(',')
        if not header:
            header = line
        else:
            if line[0] == schoolname:
                stud_directory = {}
                for i in range(1, len(line)):
                    stud_directory[header[i]] = int(line[i])
                final_list.append(stud_directory)
    return final_list

#==========================================#
# Place your student_health_list function after this line


def student_health_list(filename: str, health: str) -> list:
    """The function takes the file name where the data is stored and a health value as input parameters.
    The function returns a list of students (each student stored as a dictionary) whose health equals the
    value provided as an input parameter. The dictionary's keys are the labels for all attributes in the
    spreadsheet except “Health”. If the health value provided is not in the file, the function returns an
    empty list.

    >>> student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,
    'G1': 9, 'G2': 11, 'G3': 7},
    {another element},
    …]

    >>> student_health_list('student-mat.csv', -10)
    []
    """

    file = open(filename, 'r')
    students = []
    header = []
    line_count = 0

    for line in file:
        line = line.strip()
        if line_count == 0:

            header = line.split(",")

        else:

            row = line.split(',')

            if int(row[4]) == int(health):

                dicc = {header[i]: row[i] for i in range(len(header))}
                del dicc[header[4]]

                for key, val in dicc.items():
                    if key != header[0]:
                        dicc[key] = int(val)

                students.append(dicc)

        line_count += 1

    file.close()
    return students


#==========================================#
# Place your student_age_list function after this line


def test(filename: str) -> list[str]:
    infile = open(filename, "r")
    for line in infile:
        header = {}
        newline = str(line)
        values = newline.strip().split(",")

        print(newline)
        # for i in values:
        # print(i)

        # if i == values[1]:
        # print(i)
        # else:
        # return

        # header.update({line: line})    #this does help
        # newline = line.split()
        # print(dict(newline))


def student_age_list(filename: str, Age: int) -> list[dict]:
    """
    Return a list of students (each student stored as a dictionary) with the same age as the input parameter
    Preconditions : Age should be between 17-23 to obtain results
    >>> student_age_list("student-mat.csv", 18)
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},
    ...
    """
    infile = open(filename, "r")
    student = []
    keys = []
    for newline in infile:
        values = newline.strip().split(",")
        if values != 'GP':
            # if len(keys) < 1:
            keys += values
        if values[1] == str(Age):
            header = {}
            for i in range(len(values)):
                try:
                    value = int(values[i])
                except:
                    value = values[i]
                header[keys[i]] = value
            header.pop('Age')
            student.append(header)
    infile.close()
    return student

#==========================================#
# Place your student_failures_list function after this line


def student_failures_list(filename: str, failures: int) -> list:
    """Return a list of students with the same amount of failures as the input parameter. The keys of the dictionary are the labels for all the attributes in the spreadsheet except "Failures". If the number of failures provided is not in the file, return an empty list.
    >>> student_failures_list("student-mat.csv", 220)
    []
    >>> student_failures_list("student-mat.csv", 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'GP', 'Age': 17, 'StudyTime': 1, 'Failures': 3, 'Health': 5, 'Absences': 16, 'G1': 6, 'G2': 5, 'G3': 5}, {'School': 'GP', 'Age': 17, 'StudyTime': 1, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 19, 'StudyTime': 2, 'Failures': 3, 'Health': 5, 'Absences': 2, 'G1': 7, 'G2': 8, 'G3': 9}, {'School': 'MB', 'Age': 17, 'StudyTime': 1, 'Failures': 3, 'Health': 5, 'Absences': 0, 'G1': 5, 'G2': 0, 'G3': 0}, {'School': 'MB', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 0, 'G1': 6, 'G2': 7, 'G3': 0}, {'School': 'MB', 'Age': 15, 'StudyTime': 1, 'Failures': 3, 'Health': 5, 'Absences': 0, 'G1': 8, 'G2': 9, 'G3': 10}, {'School': 'MB', 'Age': 18, 'StudyTime': 1, 'Failures': 3, 'Health': 4, 'Absences': 0, 'G1': 6, 'G2': 5, 'G3': 0}, {'School': 'MB', 'Age': 19, 'StudyTime': 1, 'Failures': 3, 'Health': 4, 'Absences': 0, 'G1': 5, 'G2': 0, 'G3': 0}, {'School': 'MB', 'Age': 18, 'StudyTime': 1, 'Failures': 3, 'Health': 4, 'Absences': 6, 'G1': 9, 'G2': 8, 'G3': 10}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 3, 'Health': 5, 'Absences': 0, 'G1': 5, 'G2': 8, 'G3': 7}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 0, 'G1': 8, 'G2': 7, 'G3': 0}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 3, 'Health': 4, 'Absences': 5, 'G1': 7, 'G2': 7, 'G3': 7}, {'School': 'BD', 'Age': 22, 'StudyTime': 1, 'Failures': 3, 'Health': 1, 'Absences': 16, 'G1': 6, 'G2': 8, 'G3': 8}, {'School': 'MS', 'Age': 19, 'StudyTime': 2, 'Failures': 3, 'Health': 2, 'Absences': 8, 'G1': 8, 'G2': 7, 'G3': 8}, {'School': 'MS', 'Age': 21, 'StudyTime': 1, 'Failures': 3, 'Health': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7}]
    >>>student_failures_list("student-mat.csv", 9999)
    []
    """
    times = 0
    list_of_failures = []
    infile = open(filename, "r")
    for line in infile:
        line = line.strip()
        line = line.split(",")
        if times == 0:
            header = line
        elif times > 0:
            word_dict = {header[0]: "AA", header[1]: 0, header[2]: 0,
                         header[4]: 0, header[5]: 0, header[6]: 0, header[7]: 0, header[8]: 0}
            if line[3] == str(failures):
                word_dict[header[0]] = line[0]
                word_dict[header[1]] = int(line[1])
                word_dict[header[2]] = int(line[2])
                word_dict[header[4]] = int(line[4])
                word_dict[header[5]] = int(line[5])
                word_dict[header[6]] = int(line[6])
                word_dict[header[7]] = int(line[7])
                word_dict[header[8]] = int(line[8])
                list_of_failures.append(word_dict)
        times += 1
    infile.close()
    return list_of_failures

#==========================================#
# Place your load_data function after this line


def load_data(filename: str, value: tuple) -> list:
    """Return a list of students where the keys of the dictionary are the labels for all attributes in the spreadsheet except for the attribute in the first item of the tuple. If the first item of the tuple is invalid, the function will print the error message "invalid value" and return an empty list
    >>> load_data("student-mat.csv", ("Health", 3))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'GP', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 12, 'G2': 12, 'G3': 11}, {'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 10, 'G3': 11}, {'School': 'GP', 'Age': 15, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 14, 'G2': 16, 'G3': 16}, {'School': 'GP', 'Age': 16, 'StudyTime': 2, 'Failures': 1, 'Absences': 25, 'G1': 7, 'G2': 10, 'G3': 11}, {'School': 'GP', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 12, 'G1': 11, 'G2': 12, 'G3': 11}, {'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 1, 'Absences': 2, 'G1': 7, 'G2': 7, 'G3': 7}, {'School': 'GP', 'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Absences': 4, 'G1': 13, 'G2': 13, 'G3': 12}, {'School': 'GP', 'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Absences': 12, 'G1': 16, 'G2': 16, 'G3': 16}, {'School': 'GP', 'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 10, 'G3': 10}, {'School': 'GP', 'Age': 16, 'StudyTime': 4, 'Failures': 0, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}, {'School': 'GP', 'Age': 17, 'StudyTime': 1, 'Failures': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MB', 'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 1, 'Absences': 12, 'G1': 11, 'G2': 10, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 7, 'G2': 9, 'G3': 8}, {'School': 'MB', 'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Absences': 8, 'G1': 7, 'G2': 8, 'G3': 8}, {'School': 'MB', 'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Absences': 10, 'G1': 18, 'G2': 19, 'G3': 19}, {'School': 'MB', 'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Absences': 0, 'G1': 7, 'G2': 9, 'G3': 0}, {'School': 'MB', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Absences': 0, 'G1': 6, 'G2': 7, 'G3': 0}, {'School': 'MB', 'Age': 15, 'StudyTime': 3, 'Failures': 2, 'Absences': 8, 'G1': 10, 'G2': 10, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 2, 'G1': 17, 'G2': 15, 'G3': 15}, {'School': 'CF', 'Age': 15, 'StudyTime': 2, 'Failures': 2, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 14, 'G2': 15, 'G3': 16}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 13, 'G2': 15, 'G3': 16}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 3, 'Absences': 0, 'G1': 8, 'G2': 7, 'G3': 0}, {'School': 'CF', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 10, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 10, 'G1': 9, 'G2': 8, 'G3': 8}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 12, 'G2': 13, 'G3': 12}, {'School': 'CF', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 2, 'G1': 11, 'G2': 12, 'G3': 11}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 8, 'G2': 7, 'G3': 9}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 4, 'G1': 8, 'G2': 9, 'G3': 10}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 8, 'G2': 8, 'G3': 9}, {'School': 'CF', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 0, 'G1': 13, 'G2': 14, 'G3': 14}, {'School': 'CF', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 8, 'G1': 9, 'G2': 9, 'G3': 10}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 9, 'G2': 9, 'G3': 10}, {'School': 'CF', 'Age': 17, 'StudyTime': 1, 'Failures': 0, 'Absences': 18, 'G1': 7, 'G2': 6, 'G3': 6}, {'School': 'CF', 'Age': 19, 'StudyTime': 4, 'Failures': 0, 'Absences': 10, 'G1': 8, 'G2': 8, 'G3': 8}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 13, 'G1': 12, 'G2': 12, 'G3': 13}, {'School': 'CF', 'Age': 17, 'StudyTime': 1, 'Failures': 0, 'Absences': 12, 'G1': 8, 'G2': 10, 'G3': 10}, {'School': 'CF', 'Age': 17, 'StudyTime': 1, 'Failures': 0, 'Absences': 3, 'G1': 7, 'G2': 7, 'G3': 8}, {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 16, 'G2': 16, 'G3': 17}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 10, 'G1': 16, 'G2': 15, 'G3': 15}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 12, 'G2': 11, 'G3': 12}, {'School': 'CF', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 14, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'CF', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 10, 'G1': 12, 'G2': 10, 'G3': 12}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 14, 'G1': 13, 'G2': 13, 'G3': 14}, {'School': 'CF', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 13, 'G2': 11, 'G3': 11}, {'School': 'BD', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 0, 'G1': 6, 'G2': 0, 'G3': 0}, {'School': 'BD', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 7, 'G2': 0, 'G3': 0}, {'School': 'BD', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 0, 'G1': 8, 'G2': 9, 'G3': 8}, {'School': 'BD', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'School': 'BD', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}, {'School': 'BD', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 9, 'G2': 10, 'G3': 0}, {'School': 'BD', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 6, 'G2': 0, 'G3': 0}, {'School': 'BD', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 11, 'G2': 11, 'G3': 11}, {'School': 'BD', 'Age': 18, 'StudyTime': 1, 'Failures': 0, 'Absences': 22, 'G1': 9, 'G2': 9, 'G3': 9}, {'School': 'BD', 'Age': 17, 'StudyTime': 1, 'Failures': 1, 'Absences': 19, 'G1': 11, 'G2': 9, 'G3': 10}, {'School': 'BD', 'Age': 18, 'StudyTime': 4, 'Failures': 0, 'Absences': 1, 'G1': 12, 'G2': 12, 'G3': 12}, {'School': 'BD', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 12, 'G3': 12}, {'School': 'BD', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 15, 'G2': 15, 'G3': 15}, {'School': 'BD', 'Age': 17, 'StudyTime': 4, 'Failures': 0, 'Absences': 6, 'G1': 18, 'G2': 18, 'G3': 18}, {'School': 'BD', 'Age': 18, 'StudyTime': 4, 'Failures': 0, 'Absences': 0, 'G1': 14, 'G2': 13, 'G3': 14}, {'School': 'BD', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 15, 'G2': 12, 'G3': 14}, {'School': 'BD', 'Age': 19, 'StudyTime': 2, 'Failures': 1, 'Absences': 20, 'G1': 15, 'G2': 14, 'G3': 13}, {'School': 'BD', 'Age': 18, 'StudyTime': 2, 'Failures': 1, 'Absences': 8, 'G1': 14, 'G2': 12, 'G3': 12}, {'School': 'BD', 'Age': 19, 'StudyTime': 2, 'Failures': 1, 'Absences': 18, 'G1': 12, 'G2': 10, 'G3': 10}, {'School': 'BD', 'Age': 19, 'StudyTime': 2, 'Failures': 1, 'Absences': 0, 'G1': 9, 'G2': 9, 'G3': 0}, {'School': 'BD', 'Age': 19, 'StudyTime': 3, 'Failures': 2, 'Absences': 14, 'G1': 15, 'G2': 13, 'G3': 13}, {'School': 'BD', 'Age': 19, 'StudyTime': 3, 'Failures': 1, 'Absences': 40, 'G1': 13, 'G2': 11, 'G3': 11}, {'School': 'MS', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 12, 'G1': 11, 'G2': 9, 'G3': 9}, {'School': 'MS', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 3, 'G1': 11, 'G2': 11, 'G3': 11}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 3, 'G1': 9, 'G2': 12, 'G3': 11}, {'School': 'MS', 'Age': 19, 'StudyTime': 3, 'Failures': 1, 'Absences': 4, 'G1': 11, 'G2': 12, 'G3': 11}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 4, 'G1': 11, 'G2': 10, 'G3': 10}, {'School': 'MS', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 13, 'G2': 13, 'G3': 13}, {'School': 'MS', 'Age': 18, 'StudyTime': 1, 'Failures': 1, 'Absences': 7, 'G1': 8, 'G2': 7, 'G3': 8}, {'School': 'MS', 'Age': 18, 'StudyTime': 1, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 10, 'G3': 10}, {'School': 'MS', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 10}, {'School': 'MS', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 12, 'G2': 11, 'G3': 12}, {'School': 'MS', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 10, 'G3': 10}, {'School': 'MS', 'Age': 19, 'StudyTime': 2, 'Failures': 2, 'Absences': 4, 'G1': 7, 'G2': 7, 'G3': 9}, {'School': 'MS', 'Age': 18, 'StudyTime': 1, 'Failures': 0, 'Absences': 3, 'G1': 14, 'G2': 12, 'G3': 12}, {'School': 'MS', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 8, 'G1': 13, 'G2': 11, 'G3': 11}, {'School': 'MS', 'Age': 20, 'StudyTime': 3, 'Failures': 2, 'Absences': 4, 'G1': 15, 'G2': 14, 'G3': 15}, {'School': 'MS', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 2, 'G1': 11, 'G2': 11, 'G3': 10}, {'School': 'MS', 'Age': 18, 'StudyTime': 1, 'Failures': 1, 'Absences': 14, 'G1': 6, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 21, 'StudyTime': 1, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7}]
    """
    if value[0] == "School":
        return student_school_list(filename, value[1])
    elif value[0] == "Age":
        return student_age_list(filename, value[1])
    elif value[0] == "Health":
        return student_health_list(filename, value[1])
    elif value[0] == "Failures":
        return student_failures_list(filename, value[1])
    elif value[0] == "All":
        times = 0
        list_of_failures = []
        infile = open(filename, "r")
        for line in infile:
            line = line.strip()
            line = line.split(",")
            if times == 0:
                header = line
            elif times > 0:
                word_dict = {header[0]: "AA", header[1]: 0, header[2]: 0, header[3]: 0,
                             header[4]: 0, header[5]: 0, header[6]: 0, header[7]: 0, header[8]: 0}
                word_dict[header[0]] = line[0]
                word_dict[header[1]] = int(line[1])
                word_dict[header[2]] = int(line[2])
                word_dict[header[3]] = int(line[3])
                word_dict[header[4]] = int(line[4])
                word_dict[header[5]] = int(line[5])
                word_dict[header[6]] = int(line[6])
                word_dict[header[7]] = int(line[7])
                word_dict[header[8]] = int(line[8])
                list_of_failures.append(word_dict)
            times += 1
        infile.close()
        return list_of_failures
    else:
        print("Invalid Value")
        return []

#==========================================#
# Place your add_average function after this line


def add_average(students: list[dict]) -> list[dict]:
    """Return the list with the dictionaries updated with the average grade.
    >>> add_average([{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'StudyTime': 1, 'Failures': 2, 'Health': 4, 'Absences': 0, 'G1': 7, 'G2': 4, 'G3': 0}, {'School': 'MB', 'StudyTime': 1, 'Failures': 3, 'Health': 4, 'Absences': 0, 'G1': 6, 'G2': 5, 'G3': 0}])
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'School': 'MB', 'StudyTime': 1, 'Failures': 2, 'Health': 4, 'Absences': 0, 'G1': 7, 'G2': 4, 'G3': 0, 'G_Avg': 3.67}, {'School': 'MB', 'StudyTime': 1, 'Failures': 3, 'Health': 4, 'Absences': 0, 'G1': 6, 'G2': 5, 'G3': 0, 'G_Avg': 3.67}]
    """
    for i in students:
        grade1 = i.get("G1")
        grade2 = i.get("G2")
        grade3 = i.get("G3")
        G_Avg = round(((grade1 + grade2 + grade3) / 3), 2)

        i["G_Avg"] = G_Avg
    return students

# Do NOT include a main script in your submission
