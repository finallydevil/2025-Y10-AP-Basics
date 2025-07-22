# ask user for their name
username = input("what is your name?")

# ask the user for their fav number (int)
fav_num = int(input("What is your favourite number? "))

# double, halve and square the user's fav number
double = fav_num * 2
half = fav_num / 2
square = fav_num ** 2

# greet the user

print(f"\nHi {username} your favourite number is {fav_num}")

# output results of doubling, halving and squaring their fav integer
print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {half}.")
print(f"Square {fav_num} squared is {square}.")
print()
print("Have nice day.")