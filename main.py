"""
Program: Warehouse Control
Author: Nate Newport
Date: Nov. 2020
Functionality:
    - Register Products
        - id (auto generated)
        - title
        - category
        - price
        - stock

"""

# imports
from menu import clear, print_menu, print_header, print_product_info
from product import Product
import pickle

# global vars
catalog = []
next_id = []

# functions


def serialize_data():

    try:
        writer = open('warehouse.data', 'wb')
        pickle.dump(catalog, writer)
        writer.close()
        print('** Data serialized!')
    except:
        print('** Error, data not saved, DONT close the system')


def deserialize_data():
    global next_id

    try:
        reader = open('warehouse.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        last = catalog[- 1]
        next_id = last.id + 1

        how_many = len(catalog)
        print('** Read:  ' + str(how_many) + ' products')

    except:
        print('** Error, no data file found')


def register_product():
    try:
        global next_id
        print_header('Register new Product')
        title = input('Please provide the Title:  ')
        cat = input('Please provide the Category:  ')
        stock = int(input('Please provide initial Stock:  '))
        price = float(input('Please provide the Price:  '))

        # validations
        if(len(title) < 1):
            print("*Error: Title should not be empty")

        product = Product(0, title, cat, stock, price)
        next_id += 1
        catalog.append(product)
    except:
        print('** Error, try again')


def display_catalog():
    print_header('Current Catalog')
    for prod in catalog:
        print_product_info(prod)


def no_stock():
    print_header('Out of Stock')
    for prod in catalog:
        if(prod.stock == 0):
            print_product_info(prod)


def total_stock():
    print_header('Total Stock Value')
    total = 0
    for prod in catalog:
        total += (prod.price * prod.stock)

    print_header('Total Stock Value:  $' + str(total))


def cheap_stock():
    print_header('Cheapest Stock')

    cheapest = catalog[0]
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod

    print('Cheapest product is:')
    print_product_info(cheapest)


def delete_product():
    display_catalog()
    id = int(input('ID of item to delete:  '))

    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            catalog.remove(prod)
            print('** Item removed!')

    if(not found):
        print('** Incorrect ID, try again.')

    return found


def update_product_price():
    print_header('Update product price')
    display_catalog()
    id = int(input('ID of the product to update:  '))

    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            price = float(input('Please provide new price:  $'))
            prod.price = price
            print('Price Updated!')

    if(not found):
        print('** Incorrect ID, try again.')


def update_product_stock():
    print_header('Update product stock')
    display_catalog()
    id = int(input('ID of the product to update:  '))

    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            stock = int(input('Please provide new price:  $'))
            prod.stock = stock
            print('Stock Updated!')

    if(not found):
        print('** Incorrect ID, try again.')


def most_expensive_items():
    print_header('3 Most Expensive products')
    prices = []
    for prod in catalog:
        prices.append(prod.price)

    prices.sort(reverse=True)

    print(prices[0])
    print(prices[1])
    print(prices[2])


# instructions
deserialize_data()
input('Press Enter to continue...')

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option:  ')

    if(opc == '1'):
        register_product()
        serialize_data()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        no_stock()
    elif(opc == '4'):
        total_stock()
    elif(opc == '5'):
        cheap_stock()
    elif(opc == '6'):
        delete_product()
        serialize_data()
    elif(opc == '7'):
        if(update_product_price()):
            serialize_data()
    elif(opc == '8'):
        if(update_product_stock()):
            serialize_data()
    elif(opc == '10'):
        most_expensive_items()
    elif(opc == 's'):
        serialize_data()
    elif(opc == 'x'):

        input('Press Enter to continue...')


print('Good byte!')

# loop to present the menu, ask for an option
