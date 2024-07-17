# import the tabulate module for formatting the output
from tabulate import tabulate

# define a class named Shoe with the following attributes
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # define a method to return the cost of the shoes
    def get_cost(self):
        return self.cost

    # define a method to return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # define a method to return a string representation of the shoes
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

# create a variable with an empty list to store the shoes objects
shoes_list = []

# define a function to read the data from the file and create shoes objects
def read_shoes_data():
    try:
        # open the file in read mode
        file = open("inventory.txt", "r")
        # skip the first line (header)
        file.readline()
        # loop through each line in the file
        for line in file:
            # split the line by comma and strip any whitespace
            data = [item.strip() for item in line.split(",")]
            # create a shoe object with the data
            shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
            # append the shoe object to the list
            shoes_list.append(shoe)
        # close the file
        file.close()
    except Exception as e:
        # handle any error that may occur
        print(f"An error occurred: {e}")

# define a function to allow the user to capture data about a shoe and create a shoe object
def capture_shoes():
    # ask the user to enter the data for each attribute
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    # create a shoe object with the user input
    shoe = Shoe(country, code, product, cost, quantity)
    # append the shoe object to the list
    shoes_list.append(shoe)

# define a function to iterate over the shoes list and print the details of each shoe
def view_all():
    # create an empty list to store the formatted data
    table_data = []
    # loop through each shoe in the list
    for shoe in shoes_list:
        # append a list of attributes to the table data list
        table_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    # print the table data using tabulate module with headers and alignment
    print(tabulate(table_data, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="fancy_grid", numalign="right"))

# define a function to find and print the product with the highest quantity
def highest_qty():
    # initialize a variable to store the maximum quantity as zero
    max_quantity = 0
    # initialize a variable to store the index of the product with maximum quantity as -1
    max_index = -1
    # loop through each product in the list using enumerate function to get index and value
    for i, product in enumerate(shoes_list):
        # if the quantity of the current product is greater than the maximum quantity
        if product.get_quantity() > max_quantity:
            # update the maximum quantity and index variables with current values
            max_quantity = product.get_quantity()
            max_index = i
    # if there is a valid index of maximum quantity product found
    if max_index != -1:
        # print a message that this product is for sale with its details using __str__ method
        print(f"The product with the highest quantity is for sale: {shoes_list[max_index]}")

# define a function to calculate and display the total value of the inventory
def total_value():
    # create an empty list to store the formatted data
    table_data = []
    # initialize a variable to store the total value as zero
    total = 0
    # loop through each shoe in the list
    for shoe in shoes_list:
        # calculate the value of the shoe as cost times quantity
        value = shoe.get_cost() * shoe.get_quantity()
        # add the value to the total
        total += value
        # append a list of attributes and value to the table data list
        table_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity, value])
    # print the table data using tabulate module with headers and alignment
    print(tabulate(table_data, headers=["Country", "Code", "Product", "Cost", "Quantity", "Value"], tablefmt="fancy_grid", numalign="right"))
    # print the total value with formatting
    print(f"The total value of the inventory is: ${total:.2f}")

# define a main function that will run the program
def main():
    # read the shoes data from the file
    read_shoes_data()
    # print a welcome message
    print("Welcome to the shoe inventory system.")
    # use a while loop to keep the program running until the user chooses to exit
    while True:
        # print a menu of options for the user
        print("Please choose one of the following options:")
        print("1. Capture new shoe data")
        print("2. View all shoe details")
        print("3. Find the product with the highest quantity")
        print("4. Calculate and display the total value of the inventory")
        print("5. Exit the program")
        # ask the user to enter their choice
        choice = input("Enter your choice: ")
        # use if-elif-else statements to execute different functions based on the user's choice
        if choice == "1":
            # call the capture_shoes function
            capture_shoes()
        elif choice == "2":
            # call the view_all function
            view_all()
        elif choice == "3":
            # call the highest_qty function
            highest_qty()
        elif choice == "4":
            # call the total_value function
            total_value()
        elif choice == "5":
            # print a goodbye message and break the loop
            print("Thank you for using the shoe inventory system. Goodbye.")
            break
        else:
            # print an error message if the user enters an invalid choice
            print("Invalid choice. Please try again.")

# call the main function to run the program
main()