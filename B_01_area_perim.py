# Ask user for width and loop until they enter a number that's more than 0

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

# Main routine start here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")
    # calc area / perimeter
    area = width * height
    perimeter = 2 * (width + height)
    # display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")
    # ask user if they wanna keep going
    keep_going = input("Press enter to kep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator.")