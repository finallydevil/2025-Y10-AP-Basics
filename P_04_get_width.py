# Ask user for width and loop until they enter a number that's more than 0


error = "Please enter a number that's more than 0.\n"
while True:

    try:
        # ask user for a number
        width = float(input("width: "))

        # check if number is greater than 0
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)