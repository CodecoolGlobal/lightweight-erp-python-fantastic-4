""" User Interface (UI) module """
import common


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    columns_length = []
    table.insert(0, title_list)
    for column_index, column in enumerate(table[0]):
        current_max_item_length = 0
        current_column = common.get_column(table, column_index)
        for item in current_column:
            if current_max_item_length < len(item):
                current_max_item_length = len(item)
        columns_length.append(current_max_item_length)

    print_table = '/'
    whitespace_border = 1

    for columns_index, columns in enumerate(columns_length):
        print_table += (columns + whitespace_border * 2) * '-'

    print_table += (len(columns_length) - 1) * '-' + '\\\n'
    for line_index, line in enumerate(table):
        for item_index, item in enumerate(line):
            before_spaceing = ' ' * \
                ((columns_length[item_index] - len(item)) // 2)
            after_spaceing = ' ' * \
                ((columns_length[item_index] - len(item)) // 2)
            if (columns_length[item_index] - len(item)) % 2 == 1:
                before_spaceing += ' '
            print_table += '|' + whitespace_border * ' ' + before_spaceing + \
                item + after_spaceing + whitespace_border * ' '
        print_table += '|\n'
        if line_index != len(table) - 1:
            for columns in columns_length:
                print_table += '|' + (columns + whitespace_border * 2) * '-'
            print_table += '|\n'
    print_table += '\\'
    for columns_index, columns in enumerate(columns_length):
        print_table += (columns + whitespace_border * 2) * '-'

    print_table += (len(columns_length) - 1) * '-' + '/'
    print(print_table)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    if isinstance(result, str):
        print(label + result)
    else:
        print(label)
        for item in result:
            print(item)
        # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print_out = title + '\n'
    for line_index, line in enumerate(list_options):
        print_out += '    ' + '(' + str(line_index + 1) + ') ' + line + '\n'
    print_out += '    ' + '(0) ' + exit_message
    print(print_out)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for item in list_labels:
        answer = ''
        while answer == '':
            answer = input(item)
        inputs.append(answer)

    # your code

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(message)
    # your code
