""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    filename = 'hr/persons.csv'
    show_table(filename)
    options = ['Add record', 'Remove record', 'Update record', 'Get oldest person', 'Get persons closest to avarage']
    while True:
        try:
            ui.print_menu("Store manager", options, "Back to menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            filecontent = data_manager.get_table_from_file(filename)
            if option == "1":
                filecontent = add(filecontent)
            elif option == "2":
                remove_id = ui.get_inputs(
                    ['ID: '], 'Enter ID to remove item from the list'
                )[0]
                remove(filecontent, remove_id)
            elif option == "3":
                update_id = ui.get_inputs(
                    ['ID: '], 'Enter ID to update item in the list'
                )[0]
                update(filecontent, update_id)
            elif option == "4":
                ui.print_result(get_oldest_person(
                    filecontent), "Oldest person or people: ")
                ui.get_inputs([''], 'Press Enter to continue')
            elif option == "5":
                ui.print_result(get_persons_closest_to_average(filecontent), "Closest to average: ")
                ui.get_inputs([''], 'Press Enter to continue')
            elif option == "0":
                break
            elif option == '':
                raise KeyError("Please enter a valid input")
            else:
                raise KeyError("There is no such option.")
            data_manager.write_table_to_file(filename, filecontent)
            show_table(filename)
        except KeyError as err:
            show_table(filename)
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'Name', 'Birth year']
    common.show_every_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ['ID', 'Name', 'Year']
    title_list.pop(0)
    for item_index, item in enumerate(title_list):
        title_list[item_index] += ': '
    new_line = ui.get_inputs(title_list, 'Enter the following items')
    new_line.insert(0, common.generate_random(table))
    table.append(new_line)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    id_found = False

    for line_index, line in enumerate(table):
        if line[0] == id_:
            table.pop(line_index)
            id_found = True
            break

    if id_found is False:
        raise KeyError('ID not found')

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    id_found = False
    title_list = ['ID', 'Name', 'Year']
    title_list.pop(0)
    for item_index, item in enumerate(title_list):
        title_list[item_index] += ': '
    new_line = ui.get_inputs(title_list, 'Enter the following items')

    for line_index, line in enumerate(table):
        if line[0] == id_:
            new_line.insert(0, line[0])
            table[line_index] = new_line
            id_found = True
            break

    if id_found is False:
        raise KeyError('ID not found')

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    name_column = 1
    year_column = 2
    sorted_oldest_people = []
    oldest = int(table[0][year_column])
    for line in table:
        if int(line[year_column]) < oldest:
            oldest = int(line[year_column])
    for line in table:
        if int(line[year_column]) == oldest:
            sorted_oldest_people.append(line[name_column])
    return sorted_oldest_people


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    year_column = 2
    name_column = 1
    year_sum = 0
    counter = 0
    closest_to_average_year = []
    for line in table:
        year_sum += int(line[year_column])
        counter += 1
    year_average = int(year_sum/counter)
    current_person_dif = abs(year_average-int(table[0][year_column]))
    for line in table:
        dif = (int(line[year_column])-year_average)
        dif = abs(dif)
        if current_person_dif > dif:
            current_person_dif = dif
    for line in table:
        dif = (int(line[year_column])-year_average)
        dif = abs(dif)
        if dif == int(current_person_dif):
            closest_to_average_year.append(line[name_column])
    return closest_to_average_year
