# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Benjamin Robert"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101338215"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-71"

# ==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions

import sys
from load_data import *
import curve_fit
import histogram
from sort import sort
from curve_fit import *
from histogram import *
import os


def loadData():
    print("Please enter the name of the file: ", end="")
    file_name = input().strip()
    if not os.path.isfile(file_name):
        print("File not loaded. Please, load a file first.")
        data_loaded = []
        return data_loaded
    else:
        print("Please enter the attribute to use as a filter: ", end="")
        attribute = input().strip()

        if attribute.lower() != "all":
            print("Please enter the value of the attribute: ", end="")
            value = input().strip()

            # Simulated loading with filter
            print("Data loaded with filter.")
            data_loaded = (add_average(
                load_data(file_name, (attribute, value))))
            return data_loaded
        else:
            # Simulated loading without filter
            print("Data loaded without filter.")
            data_loaded = (add_average(
                load_data(file_name, (attribute))))
            return data_loaded
  # Simulate successful data load


def sort_data(data_loaded):
    print(data_loaded)
    print("Please enter the attribute you want to use for sorting ('Age', 'Failures', 'G_Avg', 'StudyTime'): ", end="")
    attribute = input().strip()
    if len(data_loaded) < 1:
        print("File not loaded. Please, load a file first.")
    else:
        print("Ascending (A) or Descending (D) order: ", end="")
        order = str(input().strip())
        print("Do you want to display the data?: ", end="")
        display = input().strip().lower()
        sort(data_loaded, order, attribute)
        if display == "y":
           # ask if they want data or the sorted data printed because the sort function only returns "List sorted"
            print(data_loaded)
            print("List sorted")
            return data_loaded
        elif display == "n":
            print("List sorted")
            return data_loaded
        else:
            print("Wrong value")


def curve(data_loaded):
    print("Please enter the attribute you want to use to find the best fit for G_Avg: ", end="")
    attribute = input().strip()
    print("Please enter the order of the polynomial to be fitted: ", end="")
    degree = input().strip()
    if len(data_loaded) < 1:
        print("File not loaded. Please, load a file first.")
    else:
        curve_fit(data_loaded, attribute, degree)


def histo(data_loaded):
    print("Please enter the attribute you want to use for plotting: ", end="")
    attribute = input().strip()
    if len(data_loaded) < 1:
        print("File not loaded. Please, load a file first.")
    else:
        histogram(data_loaded, attribute)


def main_menu():
    print("L)oad Data\nS)ort Data\nC)urve Fit\nH)istogram\nE)xit")
    print("Please type your command: ", end="")


data_loaded = []  # Tracks if the data file has been loaded


def main():

    while True:
        main_menu()
        command = input().strip().upper()
        if command == "L":
            data_loaded = loadData()
        elif command == "S":
            data_loaded = sort_data(data_loaded)
        elif command == "C":
            curve_fit(data_loaded)
        elif command == "H":
            histogram(data_loaded)
        elif command == "E":
            print("Exiting program.")
            sys.exit(0)
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
