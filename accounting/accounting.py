""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    filename = 'accounting/items.csv'
    show_table(filename)
    options = ['Add record', 'Remove record', 'Update record',
               'Highest profit year', 'Avarage profit in a given year']
    while True:
        try:
            ui.print_menu("Accounting manager", options, "Back to menu")
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
                ui.print_result(str(which_year_max(filecontent)),
                                "This year has the highest profit: ")
                ui.get_inputs([''], 'Press Enter to continue')
            elif option == "5":
                year = int(ui.get_inputs(
                    ["Year: "], "Which year's average would you like to know?")[0])
                ui.print_result(str(round(avg_amount(filecontent, year), 2)),
                                "This is the average for %s: " % year)
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
    title_list = ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount']
    common.show_every_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount']

    return common.all_add(table, title_list)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    return common.all_remove(table, id_)


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    title_list = ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount']
    
    return common.all_update(table, id_, title_list)

# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    year_column = 3
    type_column = 4
    amount_column = 5
    max_profit_year = 0
    years = []
    for line in table:
        if line[year_column] not in years:
            years.append([line[year_column], 0])
    for line in table:
        for index, year in enumerate(years):
            if line[year_column] == year[0] and line[type_column] == "in":
                years[index][1] += int(line[amount_column])
            elif line[year_column] == year[0]:
                years[index][1] -= int(line[amount_column])
    for year in years:
        if year[1] > max_profit_year:
            max_profit_year = year[1]
    for year in years:
        if year[1] == max_profit_year:
            return int(year[0])


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    year_column = 3
    type_column = 4
    amount_column = 5
    years = []
    for line in table:
        if line[year_column] not in years:
            years.append([line[year_column], 0, 0])
    for line in table:
        for index, date in enumerate(years):
            if line[year_column] == date[0] and line[type_column] == "in":
                years[index][1] += int(line[amount_column])
                years[index][2] += 1
            elif line[year_column] == date[0]:
                years[index][1] -= int(line[amount_column])
                years[index][2] += 1
    for date in years:
        if int(date[0]) == year:
            average = date[1] / date[2]
            return average
