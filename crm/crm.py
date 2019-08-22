""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    filename = 'crm/customers.csv'
    show_table(filename)
    options = ['Add record', 'Remove record', 'Update record',
               'ID of longest customer', 'Subscribed customers']
    while True:
        try:
            ui.print_menu("Customer Relationship manager",
                          options, "Back to menu")
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
                ui.print_result(get_longest_name_id(
                    filecontent), "The longest name's ID is: ")
                ui.get_inputs([''], 'Press Enter to continue')
            elif option == "5":
                ui.print_result(get_subscribed_emails(
                    filecontent), "Subscribed list is: \n")
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
    title_list = ['ID', 'Name', 'Email', 'Subscribed']
    common.show_every_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ['ID', 'Name', 'Email', 'Subscribed']

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

    title_list = ['ID', 'Name', 'Email', 'Subscribed']

    return common.all_update(table, id_, title_list)


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    names = common.get_column(table, 1)
    ordered_names = common.my_sort_(names)
    longest_name_len = 0
    longest_name = ""
    for name in ordered_names:
        if longest_name_len <= len(name):
            longest_name_len = len(name)
            longest_name = name
    id_index = 0
    for user in table:
        if longest_name in user:
            return user[id_index]


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    name = 1
    email = 2
    subscription = 3
    subscribed_list = []

    for user in table:
        if user[subscription] == '1':
            subscribed_list.append(user[email] + ";" + user[name])

    return subscribed_list
