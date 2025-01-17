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

    options = ['Get the last buyer name', 'Get the last buyer ID', 'Buyer who spent most and the money used',
               'Buyer ID who spent most and the money used', 'Most frequent buyers name',
               'Most frequent buyers ID']
    while True:
        try:
            ui.print_menu("Data Analyser", options, "Back to menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                ui.print_result(get_the_last_buyer_name(),
                                'The last buyer name:')
            elif option == "2":
                ui.print_result(get_the_last_buyer_id(), 'The last buyer ID:')
            elif option == "3":
                ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(
                ), 'The buyer who spent most and the money used:')
            elif option == "4":
                ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(
                ), 'The buyer ID who spent most and the money used')
            elif option == "5":
                ui.print_result(get_the_most_frequent_buyers_names(),
                                'Most frequent buyers name:')
            elif option == "6":
                ui.print_result(get_the_most_frequent_buyers_ids(),
                                'Most frequent buyers ID:')
            elif option == "0":
                break
            elif option == '':
                raise KeyError("Please enter a valid input")
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(str(err))

    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    filecontent = data_manager.get_table_from_file('sales/sales.csv')
    month = 3
    day = 4
    year = 5
    all_date_list = []

    for line in filecontent:
        date = line[month] + ";" + line[day] + ";" + line[year]
        all_date_list.append(date)
    dates_sorted_ = common.my_sort_(all_date_list)
    latest_date = dates_sorted_[0]
    latest_dates_list = latest_date.split(';')

    costumer_id_index = 6
    day = 1
    month = 0
    year = 2
    for data in filecontent:
        if latest_dates_list[month] in data and latest_dates_list[day] in data and latest_dates_list[year] in data:
            costumer_id = data[costumer_id_index]

    crm_filecontent = data_manager.get_table_from_file('crm/customers.csv')

    customer_name_index = 1
    for line in crm_filecontent:
        if costumer_id in line:
            output = line[customer_name_index]

    return output


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    filecontent = data_manager.get_table_from_file('sales/sales.csv')
    month = 3
    day = 4
    year = 5
    all_date_list = []

    for line in filecontent:
        date = line[month] + ";" + line[day] + ";" + line[year]
        all_date_list.append(date)
    dates_sorted_ = common.my_sort_(all_date_list)
    latest_date = dates_sorted_[0]
    latest_dates_list = latest_date.split(';')

    costumer_id_index = 6
    day = 1
    month = 0
    year = 2
    for data in filecontent:
        if latest_dates_list[month] in data and latest_dates_list[day] in data and latest_dates_list[year] in data:
            output = data[costumer_id_index]

    return output


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    sales_cust_id_column = 6
    sales_price_column = 2
    customers = {}
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for line in sales_table:
        if line[sales_cust_id_column] not in customers:
            customers[line[sales_cust_id_column]] = int(
                line[sales_price_column])
        else:
            customers[line[sales_cust_id_column]
                      ] += int(line[sales_price_column])
    max_item = 0
    max_id = ''
    for item in customers.items():
        if item[1] > max_item:
            max_item = item[1]
            max_id = item[0]
    max_customer = [max_id, max_item]

    crm_id_column = 0
    crm_customer_name_column = 1
    crm_table = data_manager.get_table_from_file('crm/customers.csv')

    for line in crm_table:
        if max_customer[0] == line[crm_id_column]:
            max_customer[0] = line[crm_customer_name_column]
            max_customer = (
                max_customer[0], max_customer[1])
            break
    return max_customer


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """
    sales_cust_id_column = 6
    sales_price_column = 2
    customers = {}
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for line in sales_table:
        if line[sales_cust_id_column] not in customers:
            customers[line[sales_cust_id_column]] = int(
                line[sales_price_column])
        else:
            customers[line[sales_cust_id_column]
                      ] += int(line[sales_price_column])
    max_item = 0
    max_id = ''
    for item in customers.items():
        if item[1] > max_item:
            max_item = item[1]
            max_id = item[0]
            max_customer = (max_id, max_item)

    return max_customer


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
