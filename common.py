""" Common module
implement commonly used functions here
"""

import random
import ui
import data_manager
import hr


def read_file(file_name):
    with open(file_name) as file:
        filecontent = file.read().splitlines()
        file.close()
    for index, line in enumerate(filecontent):
        filecontent[index] = line.split("\t")
    return filecontent


def get_column(given_list, column):
    names = []
    for index, line in enumerate(given_list):
        names.append(line[column])
    return names


def bubblesort(x, y, z=0, reversed=True):
    i = 0
    while i < len(x):
        j = 0
        while j <= (len(x) - 2):
            if x[j][z] > x[j + 1][z] and reversed is True:
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
                temp = y[j + 1]
                y[j + 1] = y[j]
                y[j] = temp
            elif x[j][z] < x[j + 1][z] and reversed is False:
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
                temp = y[j + 1]
                y[j + 1] = y[j]
                y[j] = temp
            j = j + 1
        i = i + 1
    return x, y


def bubblesort_number(x, y, reversed=True):
    i = 0
    while i < len(x):
        j = 0
        while j <= (len(x) - 2):
            if x[j] > x[j + 1] and reversed is False:
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
                temp = y[j + 1]
                y[j + 1] = y[j]
                y[j] = temp
            elif x[j] < x[j + 1] and reversed is True:
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
                temp = y[j + 1]
                y[j + 1] = y[j]
                y[j] = temp
            j = j + 1
        i = i + 1
    return x, y


def my_sort(given_list):  # only works with list of strings
    hierarchy = (
        '\t', ' ', ':', '-', ',', '&', '(', ')', ',',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    )
    max_name_lenght = 2
    hierarchyvalues = []
    for item in given_list:
        if max_name_lenght < len(item):
            max_name_lenght = len(item)
    for index, item in enumerate(given_list):
        if len(item) < max_name_lenght:
            given_list[index] += " " * (max_name_lenght - len(item))
    for line in given_list:
        indexline = []
        for letter in line[:]:
            for hierarchy_index, hierarchy_item in enumerate(hierarchy):
                if hierarchy_item == letter:
                    indexline.append(hierarchy_index)
                    break
        hierarchyvalues.append(indexline)
    for k in range(max_name_lenght - 2, -1, -1):
        alphabetcontent, given_list = bubblesort(
            hierarchyvalues, given_list, k)
    for index, item in enumerate(given_list):
        given_list[index] = item.rstrip(' ')
    return given_list


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    current_ids = get_column(table, 0)
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    generated = current_ids[0]
    while generated in current_ids:
        randomlist = []
        randomlist.append(small_letters[random.randrange(26)])
        randomlist.append(capital_letters[random.randrange(26)])
        randomlist.append(numbers[random.randrange(10)])
        randomlist.append(numbers[random.randrange(10)])
        randomlist.append(capital_letters[random.randrange(26)])
        randomlist.append(small_letters[random.randrange(26)])
        randomlist.append("#&")
        generated = ''.join(randomlist)
    return generated


def show_every_table(table, title_list):
    elements = data_manager.get_table_from_file(table)
    ui.print_table(elements, title_list)


def my_sum_(number_list):
    result = 0
    for item in number_list:
        result += item
    return result
