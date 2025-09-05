# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Liam Cooper, Arman Chowdhury, Lucas Hiscocks, Benjamin Robert"

# Update "" with your team (e.g. T102)
__team__ = "T71"

#==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(result: list, order: str) -> str:
    """ Return student list sorted in ascending or descending order based on age.
    Precondition: order == "A" or order == "D"
    >>> sort_students_age_bubble([{"Age":19,"School":"GP"},{"Age":10,"School":"MS"}], "A")
    "List sorted."
    >>> sort_students_age_bubble([{"Age":1,"School":"GP"},{"Age":100,"School":"MS"}], "A")
    "List sorted."
    >>> sort_students_age_bubble([{"Age":200,"School":"GP"},{"Age":99,"School":"MS"}], "A")
    "List sorted."
    """
    swap = True
    if result == []:
        return "Empty list."

    if not "Age" in result[0].keys():
        return "List not sorted. Age key not present."

    while swap:
        swap = False
        for i in range(len(result) - 1):
            if order == "A":
                if (result[i].get("Age") > result[i + 1].get("Age")):
                    result[i], result[i + 1] = result[i + 1], result[i]
                    swap = True

            else:
                if (result[i].get("Age") < result[i + 1].get("Age")):
                    result[i], result[i + 1] = result[i + 1], result[i]
                    swap = True
    return "List sorted."

#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(students: list[dict], order: str) -> str:
    """
    Return a list of dictionaries with students in an either descending or ascending order. If the list provided by the user is empty then return "Empty list" and If the 'order' parameter is wrong display "Invalid order specified."
    Preconditions: Order has to be either 'A' or 'D'
    >>> a = []
    >>> sort_students_time_selection (a, "D")
    <a is not modified>
    Empty list.

    >>> a = [{"StudyTime":10,"School":"GP"}, {"StudyTime":19,"School":"MS"}]
    >>> sort_students_time_selection (a, "D")
    <a is now sorted: a = [{"StudyTime": 19, "School":"MS"}, {"StudyTime":10,
    "School":"GP"}] >
    List sorted.

    >>> a = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_time_selection (a, "D")
    <a is not modified>
    List not sorted. Invalid order specified.
    """
    if len(students) == 0:
        return "Empty list."
    p = 0

    if order not in {"A", "D"}:
        return "Invalid order specified."

    for i in students:
        if ("StudyTime" in i):
            p += 1
        else:
            return "List not sorted. StudyTime key not present."
    for i in range(len(students)):
        min_position = i
        for j in range(i + 1, len(students)):
            if order == "A":
                if students[j]["StudyTime"] < students[min_position]["StudyTime"]:
                    min_position = j
            elif order == "D":
                if students[j]["StudyTime"] > students[min_position]["StudyTime"]:
                    min_position = j
        students[min_position], students[i] = students[i], students[min_position]
    return "List sorted."

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(stud_list: list[dict], grade: str) -> str:
    """Return list of students sorted by grade average in ascending or descending order.
    Precondition: grade == "A" or grade == "D"
    >>> sort_students_g_avg_insertion([{"G_Avg":19,"School":"GP"},{"G_Avg":10,"School":"MS"}], "A")
    "List sorted."
    >>> sort_students_g_avg_insertion([{"G_Avg":1,"School":"GP"},{"G_Avg":10,"School":"MS"}], "A")
    "List sorted."
    >>> sort_students_g_avg_insertion([{"G_Avg":200000,"School":"GP"},{"G_Avg":9,"School":"MS"}], "A")
    "List sorted."
    """
    if stud_list == []:
        return ('Empty list.')
    elif "G_Avg" not in stud_list[0]:
        return ("List not sorted. G_Avg key not present.")
    else:
        if grade == "A":
            for i in range(1, len(stud_list)):
                ref = stud_list[i]
                j = i - 1
                while j >= 0 and stud_list[j]["G_Avg"] > ref["G_Avg"]:
                    stud_list[j + 1] = stud_list[j]
                    j -= 1
                stud_list[j + 1] = ref
            return ('List sorted.')
        elif grade == "D":
            for i in range(1, len(stud_list)):
                ref = stud_list[i]
                j = i - 1
                while j >= 0 and stud_list[j]["G_Avg"] < ref["G_Avg"]:
                    stud_list[j + 1] = stud_list[j]
                    j -= 1
                stud_list[j + 1] = ref
            return ('List sorted.')

#==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(lst: list[dict], order: str) -> str:
    """ This function takes two input
    parameters: (1) a list of dictionaries and (2) a string (“A” or “D”) to determine if the students will
    be sorted in ascending or descending order. The function returns a string.
    The function uses the bubble sort algorithm to sort the list of students’ dictionaries by the “Failures”
    attribute.

    Preconditions: lst must be an empty list or a list of dictionaries
    values of 'Failures' must be type float or int

    >>> a = []
    >>> sort_students_failures_bubble(a, "A")
    <a is not modified>
    Empty list.
    >>> a = [{"Failures":19,"School":"GP"},{"Failures":10,"School":"MS"}]
    >>> sort_students_failures_bubble(a, "A")
    <a is now soted: a = [{"Failures": 10, "School":"MS"}, {"Failures":19,
    "School":"GP"}]>
    List sorted.
    >>> a = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_failures_bubble(a, "A")
    <a is not modified>
    List not sorted. Failures key not present.

    """
    temp_list = []
    if not lst:
        return 'Empty list.'

    elif all('Failures' not in i for i in lst):
        return "List not sorted. Failures key not present."

    else:
        # making a list of values of failures
        temp_list = [i['Failures'] for i in lst if "Failures" in i]
        if order == 'A': # bubble sorting temp_list ascending if 'A'
            for q in range(len(temp_list) - 1):
                for z in range(len(temp_list) - 1):
                    if temp_list[z] > temp_list[z + 1]:
                        temp_list[z], temp_list[z +
                                                1] = temp_list[z + 1], temp_list[z]
        elif order == 'D': # bubble sorting temp_list decsending if 'D'
            for q in range(len(temp_list) - 1):
                for z in range(len(temp_list) - 1):
                    if temp_list[z] < temp_list[z + 1]:
                        temp_list[z], temp_list[z +
                                                1] = temp_list[z + 1], temp_list[z]
        #sorting the elements of lst corisponding to the elements of temp_list
        for i in range(len(temp_list)):
            for dics in lst:
                if dics.get('Failures') == temp_list[i]:
                    index = lst.index(dics)
                    lst[index], lst[i] = lst[i], lst[index]

        return "List sorted."

#==========================================#
# Place your sort function after this line


def sort(students: list, order: str, sorting: str) -> list:
    """
    """

    if order == "A":
        if sorting == "Age":
            return sort_students_age_bubble(students, "A")

        elif sorting == "G_Avg":
            return sort_students_g_avg_insertion(students, "A")

        elif sorting == "Failures":
            return sort_students_failures_bubble(students, "A")

        elif sorting == "StudyTime":
            return sort_students_time_selection(students, "A")

        else:
            return f'Invalid input, the list cannot be sorted by {sorting}.'

    elif order == "D":
        if sorting == "Age":
            return sort_students_age_bubble(students, "D")

        elif sorting == "G_Avg":
            return sort_students_g_avg_insertion(students, "D")

        elif sorting == "Failures":
            return sort_students_failures_bubble(students, "D")

        elif sorting == "StudyTime":
            return sort_students_time_selection(students, "D")

        else:
            return f'Invalid input, the list cannot be sorted by {sorting}.'

# Do NOT include a main script in your submission
