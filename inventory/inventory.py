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
            ui.print_menu("Store manager", options, "Back to menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            filecontent = data_manager.get_table_from_file(filename)
            if option == "1":
                filecontent = add(filecontent)
            elif option == "2":
                pass
            elif option == "3":
                pass
            elif option == "4":
                pass
            elif option == "5":
                pass
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
    # your code


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

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

    # your code

    return table


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

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
