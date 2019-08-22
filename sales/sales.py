""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

    filename = 'sales/sales.csv'
    show_table(filename)
    options = ['Add record', 'Remove record', 'Update record',
               'ID of lowest price item', 'Items sold between inverval']
    while True:
        try:
            ui.print_menu("Sales manager", options, "Back to menu")
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
                ui.print_result(get_lowest_price_item_id(
                    filecontent), "ID of the item with the lowest priceing: ")
                ui.get_inputs([''], 'Press Enter to continue')
            elif option == "5":
                from_date = ui.get_inputs(
                    ['Month: ', 'Day: ', 'Year: '], 'Enter the starting date')
                for item in from_date:
                    if item.isdigit() is False:
                        raise KeyError("Please enter a valid input")
                to_date = ui.get_inputs(
                    ['Month: ', 'Day: ', 'Year: '], '\nEnter the ending date')
                for item in to_date:
                    if item.isdigit() is False:
                        raise KeyError("Please enter a valid input")
                from_date = common.value_converter_list(from_date)
                to_date = common.value_converter_list(to_date)
                ui.print_result(
                    get_items_sold_between(
                        filecontent, from_date[0], from_date[1],
                        from_date[2], to_date[0], to_date[1], to_date[2]),
                    'These items have benn sold between ' + str(from_date[0]) + '.' + str(from_date[1]) + '.' +
                    str(from_date[2]) + ' and ' + str(to_date[0]) + '.' +
                    str(to_date[1]) + '.' + str(to_date[2]) + ':'
                )
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

    title_list = ['ID', 'Title', 'Price', 'Month', 'Day', 'Year']
    common.show_every_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_list = ['ID', 'Title', 'Price', 'Month', 'Day', 'Year']
    column_number_list = [2, 3, 4, 5]
    return common.all_add(table, title_list, column_number_list)


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
    title_list = ['ID', 'Title', 'Price', 'Month', 'Day', 'Year']
    column_number_list = [2, 3, 4, 5]
    return common.all_update(table, id_, title_list, column_number_list)


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    id_column = 0
    name_column = 1
    price_column = 2
    sorted_names = []
    sorted_lowest_table = []
    lowest_price = int(table[0][price_column])
    for line in table:
        sorted_names.append(line[name_column])
        if int(line[price_column]) < lowest_price:
            lowest_price = int(line[price_column])
    sorted_names = common.my_sort_(sorted_names)
    for name in sorted_names:
        for line in table:
            if name == line[name_column] and int(line[price_column]) == lowest_price:
                sorted_lowest_table.append(line)
                break
    if len(sorted_lowest_table) == 1:
        return sorted_lowest_table[0][id_column]
    else:
        return sorted_lowest_table[-1][id_column]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    month_column = 3
    day_column = 4
    year_column = 5
    filtered_table = []
    converted_table = common.value_converter_nest(table)
    for line in converted_table:
        if year_from < line[year_column] and line[year_column] < year_to:
            filtered_table.append(line)
        elif year_from == line[year_column] or line[year_column] == year_to:
            if month_from < line[month_column] and line[month_column] < month_to:
                filtered_table.append(line)
            elif month_from == line[month_column] or line[month_column] == month_to:
                if day_from < line[day_column] and line[day_column] < day_to:
                    filtered_table.append(line)
    return filtered_table
