# ask user for the height and width

def num_check(question):

    error = "Please enter a number that's more than 0.\n"
    while True:

        try:
            # ask user for a number
            response = float(input(question))

            # check if number is greater than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine goes here...

keep_going = ""
while keep_going == "":
    # get width and height
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost / m: ")

    # calc perimeter and price for the fence
    perimeter = (width + length) * 2
    price = cost * perimeter

    # print the info
    print()
    print(f"Perimeter: {perimeter} units.")
    print(f"Price: ${price:.2f}")

    # ask user if they want to keep going
    keep_going = input("Press enter to kep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator.")
