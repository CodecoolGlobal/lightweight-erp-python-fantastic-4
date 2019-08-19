""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    filename = 'store/games.csv'
    show_table(filename)
    options = ['Add record', 'Remove record',
               'Update record', 'Game count by manufacturer',
               'Average by manufacturer']
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
                ui.print_result(get_counts_by_manufacturers(
                    filecontent).items(), 'Game count by manufacturer:')
            elif option == "5":
                manufacturer_name = ui.get_inputs(
                    ['Name: '], 'Enter the manufacturer\'s name'
                )[0]
                ui.print_result(str(get_average_by_manufacturer(
                    filecontent, manufacturer_name)), 'Game count by manufacturer: ')
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

    title_list = ['ID', 'Title', 'Manufacturer', 'Price', 'In stock']
    common.show_every_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ['ID', 'Title', 'Manufacturer', 'Price', 'In stock']
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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    id_found = False
    title_list = ['ID', 'Title', 'Manufacturer', 'Price', 'In stock']
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

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    games_by_manufacturer = {}
    manufacturers = common.get_column(table, 2)
    for manufacturer in manufacturers:
        if manufacturer in games_by_manufacturer:
            games_by_manufacturer[manufacturer] += 1
        else:
            games_by_manufacturer[manufacturer] = 1
    return games_by_manufacturer


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    manufacturer_found = False
    manufacturer_column = 2
    in_stock_column = 4
    manufacturer_table = []
    for line in table:
        if manufacturer in line[manufacturer_column]:
            manufacturer_table.append(line)
            manufacturer_found = True

    if manufacturer_found is False:
        raise KeyError('Manufacturer not found')

    manufacturer_in_stock = common.get_column(
        manufacturer_table, in_stock_column)
    for item_index, item in enumerate(manufacturer_in_stock):
        manufacturer_in_stock[item_index] = int(item)
    return (common.my_sum_(manufacturer_in_stock) / len(manufacturer_in_stock))
