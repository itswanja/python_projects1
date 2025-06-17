# Exercise 1 Rectangle area calc
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is {area}cm^2")

# Exercise 2 Shopping cart program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")

# Madlibs game - word game where you create a story by filling in blanks with a random word

adjective1 = input("Enter an adjective (description of something): ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter an adjective (description of something): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description of something): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"The {noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")