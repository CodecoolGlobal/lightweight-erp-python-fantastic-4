""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

    filename = 'inventory/inventory.csv'
    show_table(filename)
    options = ['Add record', 'Remove record', 'Update record', 'Get available items',
               'Get avarage durability by manufacturers']
    while True:
        try:
            ui.print_menu("Inventory manager", options, "Back to menu")
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
                year = int(ui.get_inputs(
                    ['Year:'], 'Enter durability date')[0])
                ui.print_result(get_available_items(
                    filecontent, year), "Items have not exceeded their durability: ")
                ui.get_inputs([''], 'Press Enter to continue')
            elif option == "5":
                ui.print_result(get_average_durability_by_manufacturers(
                    filecontent), "Avarage durability by manufacturers: ")
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

    title_list = ['ID', 'Name', 'Manufacturer', 'Purchase Year', 'Durability']
    common.show_every_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_list = ['ID', 'Name', 'Manufacturer', 'Purchase year', 'Durability']
    column_number_list = [3, 4]
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
    title_list = ['ID', 'Name', 'Manufacturer', 'Purchase year', 'Durability']
    column_number_list = [3, 4]
    return common.all_update(table, id_, title_list, column_number_list)


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    durability_column = 4
    year_column = 3
    filtered_list = []
    for line in table:
        if year <= int(line[year_column]) + int(line[durability_column]):
            filtered_list.append(line)
    filtered_list = common.value_converter_nest(filtered_list)
    return filtered_list


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    manufacturer_column = 2
    durability_column = 4
    manufacturers = {}
    for line in table:
        if line[manufacturer_column] not in manufacturers:
            manufacturers[line[manufacturer_column]] = [
                1, int(line[durability_column])]
        else:
            manufacturers[line[manufacturer_column]] = [manufacturers[line[manufacturer_column]]
                                                        [0] + 1, manufacturers[line[manufacturer_column]][1] + int(line[durability_column])]
    for key, value in manufacturers.items():
        manufacturers[key] = value[1] / value[0]
    return manufacturers
