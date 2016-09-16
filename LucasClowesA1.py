"""   IT@JCU CP1404 Assignment 1 from 2016
    Shopping List Lucas Clowes
    14/09/2016
https://github.com/LucasClowes/Assessment-1-

psuedocode:
    function main()
    open csv
    display welcome message
    display menu
    get choice
    while choice is not 'q'
        if choice is 'r'
            send choice to function print list()
        else if choice is 'c'
            send choice to function print list()
        else if choice is 'a'
            function add_list()
        else if choice is 'm'
            function print_list()
            function mark_item()
        else
            display invalid choice message
        display menu
        get choice
    save csv
    print farewell message

function print_list()
    if flag == "r":
        print 'required items'
    elif flag == "c":
        print 'completed items'
    elif flag == "m":
        change flag to 'r'
    count = 0
    total = 0
    for item in shopping_list:
        if flag in item[3]:
            print each entry in shopping_list that has teh flag in slot 3
            count += 1
            total += prices of the entry added up

    if count == 0:
        if flag == "r":
            print 'no required items'
        elif flag == "c":
            print 'no completed items'
        else:
            print 'no items in list'
    else:
        print ' total expected items (count) , (price)







function mark_item()
    get number from user
    while not item_number.isdigit():
        print invalid entry
        get number from user
    count = 0
    total = 0
    while total == 0:
        for item in shopping_list:
            if item[3] == "r":
                if count == item_number:
                    item[3] = "c"
                    print item[0], 'marked as completed'
                elif count == 0:
                    print invalid entry
                    get number from user
                else:
                    total += 1
function add item()
     item_list = []
    get item name
    while not item_name.isalnum():
        print invalid input
        get item name

    add item_name to item_list
    valid_no = False
    while not valid_no:
        get price
        a_number = is_number(price)
        if not a_number:
            print invalid input
        elif float(price) < 0:
            print Price must be >= 0
        else:
            valid_no = True
    add price to item_list

    valid_priority = False
    while not valid_priority:
        get priority
        a_digit = priority.isdigit()
        if not a_digit:
            print invalid number
        elif int(priority) < 0:
            print Priority must be 1, 2 or 3
        else:
            valid_priority = True
    add priority to item_list
    add 'r' to item_list

    add item_list to shopping_list
    print item_name price priority

"""

import csv

MENU = "\nMenu:\n R - List of Required Items\n C - List of Completed Items\n A - Add New Item\n" \
       " M - Mark an Item as Completed\n Q - Quit"


def main():
    with open('items.csv', 'r') as f:
        reader = csv.reader(f)
        shopping_list = list(reader)
        shopping_list.sort()
    print('Shopping List 1.0 - By Lucas Clowes')
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "R":
            print_list(shopping_list, choice.lower())
        elif choice == "C":
            print_list(shopping_list, choice.lower())
        elif choice == "A":
            add_item(shopping_list)
        elif choice == "M":
            print_list(shopping_list, choice.lower())
            mark_item(shopping_list)
        else:
            print("Invalid Menu Choice")
        print(MENU)
        choice = input(">>>").upper()
    with open("items.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(shopping_list)
    print("Have a nice day!")


def print_list(shopping_list, flag):
    #takes the users choice from the menu and determines which way to handle it through if statements.
    if flag == "r":
        print("Required Items:")
    elif flag == "c":
        print("Completed Items")
    elif flag == "m":
        flag = "r"
    count = 0
    total = 0
    for item in shopping_list:
        if flag in item[3]:
            print("{}. {:20}   $ {:10} ({})".format(count, item[0], item[1], item[2], item[3]))
            count += 1
            total += float(item[1])
    # checks each entry for the flag/choice from user and prints the result
    if count == 0:
        if flag == "r":
            print("No Required Items")
        elif flag == "c":
            print("No Completed Items")
        else:
            print("No Items In List")
    else:
        print("Total expected price for {} items: ${}".format(count, total))


def mark_item(shopping_list):
    #Asks the user to choose a entry within the shopping list to mark as completed
    valid_itemnumber = False
    while not valid_itemnumber:
        item_number = int(input("Enter the Number of an Item to Mark as Completed"))
        count = -1
        for item in shopping_list:
            if item[3] == "r":
                count+=1
                if count == item_number:
                    item[3] = "c"
                    print(item[0], "Marked as Completed")
                    valid_itemnumber = True
                    break
            elif count==item_number :
                print("Error, item not marked as required")
                valid_itemnumber = True
                break
        if not valid_itemnumber:
            print("Invalid item number")


def is_number(price):
    # Checks if the price the user inputted is a float
    try:
        float(price)
        return True
    except ValueError:
        pass
    return False


def add_item(shopping_list):
    #Gets input from user about adding a new item to the shopping list; error checking to decide if user inputs match
    #what is required.
    item_list = []
    item_name = str(input("Item name: "))
    while not item_name.isalnum():
        print("Input cannot be Blank")
        item_name = str(input("Item name: "))
    # item_name holds the entry
    item_list.append(item_name)
    valid_no = False
    while not valid_no:
        price = (input("Price: $"))
        a_number = is_number(price)
        if not a_number:
            print("Invalid Input: enter a valid number")
        elif float(price) < 0:
            print("Price must be >= 0")
        else:
            valid_no = True
    item_list.append(price)
    # price holds the valid number

    valid_priority = False
    while not valid_priority:
        priority = (input("Priority: "))
        a_digit = priority.isdigit()
        if not a_digit:
            print("Invalid Input: enter a valid number")
        elif int(priority) < 0:
            print("Priority must be 1, 2 or 3")
        else:
            valid_priority = True
    item_list.append(priority)
    item_list.append("r")
    # priority holds the valid entry
    shopping_list.append(item_list)
    print("{}, ${} (Priority {}) added to shopping list".format(item_name, float(price), priority))


main()
