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

# main thing goes here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    Height = num_check("Height: ")
    print(Height)