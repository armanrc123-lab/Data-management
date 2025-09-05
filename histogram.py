# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Liam Cooper"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101342043"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-71"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt
import numpy
from collections import Counter


def histogram(students, attribute):
    """Return bar graph of given data as well as: the max value of the value associated with attribute from within the list of students if attribute is an int or float, or -1 if attribute is a categorical piece of information.
    >>> histogram([{"Age": 19, "School": "MB"}, {"Age": 11, "School": "MB"}, {"Age": 20, "School": "MB"}], "Age")
    20
    >>> histogram([{"Age": 20, "School": "MB"}, {"Age": 11, "School": "MB"}, {"Age": 20, "School": "GP"}], "School")
    -1
    >>> histogram([{"Health": 1, "School": "MB"}, {"Health": 11, "School": "MB"}, {"Health": 200, "School": "MB"}], "Age")
    200
    """
    # Extract the attribute values from the data
    attribute_values = [student[attribute] for student in students]

    # CATEGORICAL
    if isinstance(attribute_values[0], str):
        counts = Counter(attribute_values)
        bins = list(counts.keys())
        bin_labels = list(counts.values())  # creates labels

        fig1 = plt.figure()
        plt.bar(bins, bin_labels, color="purple")
        plt.title(f"Histogram of {attribute}")
        plt.xlabel(attribute)
        plt.ylabel("# of Students")
        plt.show()
        return -1 #Return -1

    # NUMERICAL
    elif isinstance(attribute_values[0], (int, float)):
        bins = numpy.linspace(0, max(attribute_values),
                              11) # creates 10 dvisions
        bin_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #initiate empty bins

        for value in attribute_values:
            for i in range(len(bins) - 1):
                if bins[i] <= value < bins[i + 1]:
                    bin_numbers[i] += 1
                    break
            if value == max(attribute_values):
                bin_numbers[-1] += 1

        fig1 = plt.figure()
        plt.bar([bins[0], bins[1], bins[2], bins[3],
                 bins[4], bins[5], bins[6], bins[7], bins[8], bins[9]], bin_numbers, color="purple")
        plt.title(f"Histogram of {attribute}")
        plt.xlabel(attribute)
        plt.ylabel("Students")
        plt.show()
        return max(attribute_values) # Return max value


# Do NOT include a main script in your submission
