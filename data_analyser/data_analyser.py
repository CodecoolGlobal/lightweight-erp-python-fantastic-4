"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm
import data_manager


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code
    sales_cust_id_column = 6
    customers = {}
    customers_list = []
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for line in sales_table:
        if line[sales_cust_id_column] not in customers:
            customers[line[sales_cust_id_column]] = 1
        else:
            customers[line[sales_cust_id_column]] += 1

    for customer in range(num):
        max_item = 0
        max_id = ''
        for item in customers.items():
            if item[1] > max_item:
                max_item = item[1]
                max_id = item[0]
        customers_list.append([max_id, max_item])
        customers.pop(max_id)

    crm_id_column = 0
    crm_customer_name_column = 1
    crm_table = data_manager.get_table_from_file('crm/customers.csv')

    for index, item in enumerate(customers_list):
        for line in crm_table:
            if item[0] == line[crm_id_column]:
                customers_list[index][0] = line[crm_customer_name_column]
                customers_list[index] = (
                    customers_list[index][0], customers_list[index][1])
                break
    return customers_list


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """
    cust_id_column = 6
    customers = {}
    customers_list = []
    filecontent = data_manager.get_table_from_file('sales/sales.csv')
    for line in filecontent:
        if line[cust_id_column] not in customers:
            customers[line[cust_id_column]] = 1
        else:
            customers[line[cust_id_column]] += 1

    for customer in range(num):
        max_item = 0
        max_id = ''
        for item in customers.items():
            if item[1] > max_item:
                max_item = item[1]
                max_id = item[0]
        customers_list.append((max_id, max_item))
        customers.pop(max_id)
    # your code
    return customers_list
